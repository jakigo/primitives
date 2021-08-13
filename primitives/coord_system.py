import numpy as np
from primitives.vector import Vector
from primitives.point import Point
class CoordSystem:
    def __init__(self, vectorA = Vector().unit(), vectorB = Vector(Point(),Point(0,1,0))):
        self.vectorA = vectorA
        self.vectorB = vectorB
        
    def as_numpy(self, axis=0):
        def build_matrix(a, b, c, axis=0):
            comp = ([a,b,c] + [a,b,c])[axis:axis+3]
            def bl(num):
                return [x[num] for x in comp]
            return [ bl(x) for x in range(3) ]
        origin, v0 = self.vectorA.as_numpy()
        #v1 = self.vectorB.as_numpy_direction()
        #v2 = np.cross(v0, v1)
        v0v = self.vectorA.normalize().as_numpy()[1]
        v2v = self.vectorB.normalize().as_numpy()[1]
        v3v = Vector().from_numpy_direction(np.cross(v0v, v2v)).normalize().as_numpy()[1]
        v4v = np.cross(v3v,v0v)
        bum = np.array(build_matrix(v0v,v4v,v3v, axis))
        return origin, bum
        
    def as_numpy_inverse(self, axis=0):
        origin, mat = self.as_numpy(axis)        
        return origin, np.linalg.inv(mat)
        
    def project_point(self, point, axis=0):
        origin, mat = self.as_numpy_inverse(axis)
        origin = Point().from_numpy(origin)
        point = point.sum(origin.multiply(-1))
        point = Point().from_numpy(np.matmul(mat,point.as_numpy()))
        #point = point.sum(origin) 
        
        
        return point
        
    def de_project_point(self, point, axis=0):
        origin, mat = self.as_numpy(axis)
        origin = Point().from_numpy(origin)
        #point = point.sum(origin.multiply(-1))
        point = Point().from_numpy(np.matmul(mat, point.as_numpy()))
        point = point.sum(origin) 
        return point
        
    def project_vector(self, vector, axis=0):
        return Vector(self.project_point(vector.pointA, axis),self.project_point(vector.pointB, axis))

    def de_project_vector(self, vector, axis=0):
        return Vector(self.de_project_point(vector.pointA, axis),self.de_project_point(vector.pointB, axis))

    def get_plane(self, axis = 0):
        point = [ [0,0,1],[0,1,0],[1,0,0] ][axis]
        return self.project_vector(Vector(Point(), Point(*point)))
        
        

        
    def __str__(self):
        mat = self.as_numpy()
        return f"""
        <{self.vectorA} {self.vectorB}>
    
        {mat}
        """