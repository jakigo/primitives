from maker.parameter_basket import get_parameter, set_parameter, add_parameter
from shape.polygon_holes import PolygonHole
from shape.polygon import Polygon
from primitives.point import Point
from maker.utils import *
import numpy as np
import trimesh
from shapely.geometry import Polygon as SPoly
import triangle as tr

class Mesh:
    def __init__(self):
        self.mesh_name = add_parameter("meshname", "tests/cube.obj")
        mesh = trimesh.load(get_parameter(self.mesh_name))
        self.faces = []

        def ordered_union(arrays):
            vectors = [[(s,e) for s,e in zip(arr[:-1],arr[1:]) ]   for arr in arrays]
            [vv.append((vv[-1][1],vv[0][0]))   for vv in vectors]

            vectors = [x for y in vectors for x in y]


            def remove_duplicate(vect):

                result = {}
                tuples = {}
                for vv in vect:
                    kk = frozenset(vv)
                    result[kk] = result.get(kk,0) + 1
                    tuples[kk] = vv
                return [tuples[k] for k,v in result.items() if v == 1]
            vectors = remove_duplicate(vectors)
            starts = {x[0]:x for x in vectors}
            def find_next(fromz, done, starts):
                nextz = starts[fromz[1]]
                if nextz[0] in done:
                    return [fromz]
                done += [fromz[0]]
                return [fromz] + find_next(nextz, done, starts)

            vectors = find_next(vectors[0], [], starts)



            
            #import ipdb;ipdb.set_trace()
            return [x[0] for x in vectors]

        faces_vertices = []
        for face in mesh.facets:
            vertices = mesh.vertices[ordered_union(mesh.faces[face])]
            faces_vertices.append(vertices)
            self.faces.append(Face(vertices))

        
        edge_to_face = {}
        for face in faces_vertices:
            
            for a, b in zip(face.tolist(), face[1:].tolist() + [face[0].tolist()]):
                key = frozenset([tuple(a), tuple(b)])
                edge_to_face[key] = edge_to_face.get(key, []) + [face]
        
        for ((keyA, keyB), (fa, fb)) in edge_to_face.items():
            self.faces.append(Junction(np.array([keyA, keyB]), fa, fb))

    def eval(self):
        meshes = []
        for face in self.faces:
            meshes.append(face.eval())
        
        mesh = meshes[0]
        for mm in meshes[1:]:
            if mm != None:
                mesh += mm
        return mesh


class Junction:
    pass    


class Face:
    def extract_used_vars(self):
        allz = vars(self)
        returnz = []
        for k,v in allz.items():
            if k == "old_values":
                continue
            if type(v) == str:
                returnz.append(v)
            if type(v) == list:
                returnz += v
        returnz = [get_parameter(x) for x in returnz]
        return returnz
    def __init__(self, vertices):
        self.depth = add_parameter("depth", 0.1)
        self.internal_hole = add_parameter("internalhole", 0.1)
        self.visible = add_parameter("visible", True)
        self.triangulate = add_parameter("triangulate", 'qa0.02')
        self.triangulate_debuffer = add_parameter("triangulatedebuffer", -0.015)
        self.inbuffer = add_parameter("inbuffer", 0)
        self.outbuffer = add_parameter("outbuffer", 0)
        
        self.junction_holes_position = [add_parameter(f"junctionA{x}position", 0.33) for x in range(len(vertices))]
        self.junction_hole2_position = [add_parameter(f"junctionB{x}position", 0.66) for x in range(len(vertices))]
        self.junction_holes_height = [add_parameter(f"junctionA{x}height", 0.01) for x in range(len(vertices))]
        self.junction_hole2_height = [add_parameter(f"junctionB{x}height", 0.01) for x in range(len(vertices))]
        self.junction_holes_dist = [add_parameter(f"junctionA{x}dist", 0.01) for x in range(len(vertices))]
        self.junction_hole2_dist = [add_parameter(f"junctionB{x}dist", 0.01) for x in range(len(vertices))]
        self.junction_holes_lenght = [add_parameter(f"junctionA{x}lenght", 0.01) for x in range(len(vertices))]
        self.junction_hole2_lenght = [add_parameter(f"junctionB{x}lenght", 0.01) for x in range(len(vertices))]            

        


        self.vertices = vertices #add_parameter("vertices",[x for x in vertices])
        self.old_values = [None for x in self.extract_used_vars()]
        

        

    def is_like_old(self):
        
        return all([x == y for x,y in zip(self.old_values, self.extract_used_vars() )])
        
    def update_old(self):
        self.old_values = self.extract_used_vars()
    
    def eval(self):
        if self.is_like_old():
            return self.mesh
        self.mesh = self.eval_internal()
        print("regen")
        self.update_old()
        return self.mesh

    def eval_internal(self):
        if not get_parameter(self.visible):
            return None

        poly = PolygonHole(Polygon([Point(*x) for x in self.vertices]))
        coord = poly.get_coord_system()
        shape = poly.as_shapely()
        shape = shape.buffer(get_parameter(self.inbuffer)).buffer(get_parameter(self.outbuffer))
        def create_junc_hole(vector, position, dist, height, lenz):
            point = vector.point_from_interpolation(position)
            dirx = vector.normalize()
            diry = dirx.rot90().rot90().rot90()
            
            p0 = point.sum(diry.multiply(dist).pointB).sum(dirx.multiply(lenz/2).pointB).as_numpy()
            p1 = point.sum(diry.multiply(dist).pointB).sum(dirx.multiply(lenz/-2).pointB).as_numpy()
            p2 = point.sum(diry.multiply(dist + height).pointB).sum(dirx.multiply(lenz/2).pointB).as_numpy()
            p3 = point.sum(diry.multiply(dist + height).pointB).sum(dirx.multiply(lenz/-2).pointB).as_numpy()
            return np.array([p0,p1,p3,p2])          

        junc_holes = []
        for i, vect in enumerate(poly.shape.to_2d_vectors()):
            junction_holes_position = get_parameter(self.junction_holes_position[i])
            junction_holes_height = get_parameter(self.junction_holes_height[i])
            junction_holes_dist = get_parameter(self.junction_holes_dist[i])
            junction_holes_lenght = get_parameter(self.junction_holes_lenght[i])
            points_hole = create_junc_hole(vect, junction_holes_position, junction_holes_dist, junction_holes_height, junction_holes_lenght)
            junc_holes.append(SPoly(points_hole))

            junction_holes_position = get_parameter(self.junction_hole2_position[i])
            junction_holes_height = get_parameter(self.junction_hole2_height[i])
            junction_holes_dist = get_parameter(self.junction_hole2_dist[i])
            junction_holes_lenght = get_parameter(self.junction_hole2_lenght[i])
            points_hole = create_junc_hole(vect, junction_holes_position, junction_holes_dist, junction_holes_height, junction_holes_lenght)
            
            junc_holes.append(SPoly(points_hole))





        hole = poly.as_shapely() 
        hole = SPoly(hole.exterior.coords, [x.exterior.coords for x in junc_holes]).buffer(0)
        
        hole = hole.buffer(get_parameter(self.internal_hole) * -1)
        hole2 = hole.buffer(get_parameter(self.internal_hole) * -1)

        
        
        A = dict(vertices=np.array(hole.exterior.coords))
        B = tr.triangulate(A, get_parameter(self.triangulate))
        
        B = [SPoly([B["vertices"][i]  for i in tri])  for tri in B["triangles"]]
        B = [x.buffer(get_parameter(self.triangulate_debuffer)) for x in B]

        for bb in B:
            hole = hole.difference(bb)
        hole = hole2.difference(hole)
        
        shape = shape.difference(hole)
        
        
        for bb in junc_holes:
            shape = shape.difference(bb)
        #poly.from_shapely(shape).plot()
        #import ipdb;ipdb.set_trace()
        #
        #shape = SPoly(shape.exterior.coords, [x.exterior.coords for x in B] ).buffer(0)
          

        mesh = trimesh.creation.extrude_polygon(shape, get_parameter(self.depth))
        mesh.vertices = [coord.de_project_point(Point(*x)).as_numpy() for x in mesh.vertices]

        return mesh
        #



