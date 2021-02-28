import unittest
from src.model import Point
from src.pie import Pie

from parameterized import parameterized


class PieTestCase(unittest.TestCase):
    @parameterized.expand([
        (0, 55, 55, False),
        (12, 55, 55, False),
        (13, 55, 55, True),
        (99, 99, 99, False),
        (87, 20, 40, True),
        (25, 55, 50, True),  # on x axis
        (50, 50, 40, True),  # on negative y axis
        (75, 45, 50, True),  # on negative x axis
        (1, 50, 50, True),
        (1, 50, 100, True),  # on circumference
        (1, 50, 101, False),  # just outside circumference
        (100, 49, 99, True),
        (100, 0, 0, False)
    ])
    def test_pie_for_given_circle_should_yield_expected_result(self, percent, x, y, expected):
        pie = Pie(Point(50, 50), 90, 50)  # Code is tested only for this configuration
        actual = pie.is_inside(Point(x, y), percent)

        self.assertEqual(expected, actual)

    def test_pie_for_given_circle_config_clockwise_is_supported(self):
        pie = Pie(Point(50, 50), 90, 50, 'clock_wise')  # Code is tested only for this configuration
        actual = pie.is_inside(Point(25, 25), 75)

        self.assertEqual(True, actual)

    def test_pie_for_given_circle_config_anti_clockwise_is_not_supported(self):
        pie = Pie(Point(50, 50), 90, 50, 'anti_clock_wise')  # Code is tested only for this configuration
        self.assertRaises(Exception, lambda: pie.is_inside(Point(25, 25), 75))


if __name__ == '__main__':
    unittest.main()
