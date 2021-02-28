import math


class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_angle_in_degree(self):
        if self.x == 0:
            radians = math.pi/2 if self.y > 0 else 3 * math.pi / 2
        else:
            radians = math.atan(self.y / self.x)

        return (radians * 180) / math.pi

    def distance_from_center(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))


class Range:
    def __init__(self, frm, to):
        self._frm = frm
        self._to = to

    def in_range(self, given_angle):
        return self._frm <= given_angle <= self._to
