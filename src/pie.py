from src.model import Range

default_direction = 'clock_wise'


class Pie:
    def __init__(self, center, start_angle, radius, direction=None):
        self._center = center
        self._start_angle = start_angle
        self._radius = radius
        self._direction = default_direction if direction is None else direction

    def is_inside(self, point_to_check, progress_percent):
        relative_point = point_to_check - self._center  # moving the point relative to Point(0, 0)

        polar_radius = relative_point.distance_from_center()
        if polar_radius > self._radius:
            return False

        if progress_percent == 100:
            return polar_radius <= self._radius

        if progress_percent == 0:
            return False

        if progress_percent > 0 and point_to_check == self._center:
            return True

        end_angle = self.__get_end_angle(progress_percent)
        given_angle = relative_point.get_angle_in_degree()

        return self.__is_inside_covered_region(end_angle, given_angle)

    def __get_end_angle(self, progress_percent):
        if self._direction == default_direction:
            return (self._start_angle - (360 / 100) * progress_percent + 360) % 360
        else:
            return (self._start_angle + (360 / 100) * progress_percent + 360) % 360

    def __is_inside_covered_region(self, end_angle, given_angle):
        if self._direction == default_direction:
            black_ranges = self.__get_ranges_which_is_covered(end_angle)
            for angle_range in black_ranges:
                if angle_range.in_range(given_angle):
                    return True

            return False
        else:
            raise ValueError(self._direction)

    def __get_ranges_which_is_covered(self, end_angle):
        if self._direction == default_direction:
            if self._start_angle == 0 and end_angle == 0:
                return [Range(0, 0)]
            if self._start_angle == 0 and end_angle == 360:
                return [Range(0, 360)]
            if self._start_angle == 0 and end_angle != 0:
                return [Range(end_angle, 360)]
            if self._start_angle > 0 and self._start_angle > end_angle >= 0:
                return [Range(end_angle, self._start_angle)]
            if 0 < self._start_angle < end_angle:
                return [Range(0, self._start_angle), Range(end_angle, 360)]
        else:
            raise ValueError(self._direction)
