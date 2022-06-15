from django.contrib.gis.geos import Point, Polygon
from ..models import Provider

point_1 = Point(5, 3)  # polygon_1, polygon_2 contain this point
point_2 = Point(100, 56)  # No polygon contains this point
polygon_1 = Polygon(
    ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)))

polygon_2 = Polygon(
    ((0.0, 0.0), (0.0, 40.0), (40.0, 40.0), (40.0, 0.0), (0.0, 0.0)))
