import math
import importlib.util
import sys
from pathlib import Path


module_path = Path('LAB   Points on a plane.py').resolve()
spec = importlib.util.spec_from_file_location("my_module", module_path)
my_module = importlib.util.module_from_spec(spec)
sys.modules["my_module"] = my_module
spec.loader.exec_module(my_module)
Point = my_module.Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3



    def perimeter(self):
        perimeter = 0
        perimeter += self.__vertice1.distance_from_point(self.__vertice2)
        perimeter += self.__vertice2.distance_from_point(self.__vertice3)
        perimeter += self.__vertice3.distance_from_point(self.__vertice1)
        return perimeter




triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
