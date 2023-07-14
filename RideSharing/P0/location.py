from typing import Tuple


class Location:

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self._x = x_coordinate
        self._y = y_coordinate

    def position(self) -> Tuple[int, int]:
        return self._x, self._y
