import unittest
from primitives.point import Point
from shape.polygon import Polygon
from shape.polygon_holes import PolygonHole


class TestPolygon(unittest.TestCase):

    def test_create(self):
        p0 = Point(0,0,0)
        p1 = Point(10,0,0)
        p2 = Point(10,10,0)
        p3 = Point(0,10,0)

        h0 = Point(1,1,0)
        h1 = Point(9,1,0)
        h2 = Point(9,9,0)
        h3 = Point(1,9,0)
        poly = PolygonHole(Polygon([p0,p1,p2,p3]), holes=[Polygon([h0,h1,h2,h3])])
        #shap = poly.as_shapely()
        #poly.plot()

    def test_to_from_shapely(self):
        def assertPointArray(a, b):
            def assertPoints(alfa,beta):
                print(alfa)
                print(beta)
                self.assertEqual(alfa.x, beta.x)
                self.assertEqual(alfa.y, beta.y)
                self.assertEqual(alfa.z, beta.z)
            [assertPoints(g, h) for g,h in zip(a,b)]
        p0 = Point(0,0,3)
        p1 = Point(10,0,3)
        p2 = Point(10,10,3)
        p3 = Point(0,10,3)

        h0 = Point(1,1,3)
        h1 = Point(9,1,3)
        h2 = Point(9,9,3)
        h3 = Point(1,9,3)
        poly = PolygonHole(Polygon([p0,p3,p2,p1]), holes=[Polygon([h0,h1,h2,h3])])
        shap = poly.as_shapely()
        shap2 = poly.from_shapely(shap)
        po = shap2.shape.to_point_array()
        ho = shap2.holes[0].to_point_array()
        assertPointArray([p0,p1,p2,p3],po)
        assertPointArray([h0,h3,h2,h1],ho)



        
        

if __name__ == '__main__':
    unittest.main()