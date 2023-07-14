from location import Location
from math import sqrt


class DistanceCalculator:
    """ Distance between any two position in 2D space. """
    def __init__(self, position_one: Location, position_two: Location):
        self.starting_point = position_one.position()
        self.end_point = position_two.position()

    def euclidean_distance(self):
        x1, y1 = self.starting_point
        x2, y2 = self.end_point
        # print(f"Calculating eucledian distance for x1 {x1} y1 {y1} x2 {x2} y2 {y2} -> {sqrt((x2-x1)**2 + (y2-y1)**2)}")
        return sqrt((x2-x1)**2 + (y2-y1)**2)
