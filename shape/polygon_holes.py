from shape.polygon import Polygon
from primitives.vector2d import Vector2d
from primitives.point2d import Point2d
from shapely.geometry import Polygon as SPoly
class PolygonHole:
    def __init__(self, shape, holes=[]):
        self.shape = shape
        self.holes = holes

    def as_shapely(self, coord = None):
        if coord == None:
            coord = self.shape.get_coord_system()
        points = [x.pointA.as_numpy() for x in self.shape.to_2d_vectors(coord)]
        holes = [[x.pointA.as_numpy() for x in y.to_2d_vectors(coord)] for y in self.holes]
        return SPoly(points, holes).buffer(0)

    def plot(self):
        import matplotlib.pyplot as plt
        import geopandas as gpd
        p = gpd.GeoSeries(self.as_shapely())
        p.plot()
        plt.show()

    def get_coord_system(self):
        return self.shape.get_coord_system()
    def from_shapely(self, spoly, coord=None):
        if coord == None:
            coord = self.shape.get_coord_system()
        def vect_from_points(points, coord):
            pre_vectors = [ Vector2d(Point2d(*s),Point2d(*e)) for s,e in zip(points[:-1],points[1:]) ]
            poly = Polygon().from_2d_vectors(pre_vectors, coord)
            return poly
        return PolygonHole(vect_from_points(spoly.exterior.coords, coord), holes = [vect_from_points(x.coords, coord) for x in spoly.interiors])
    
