import console_io
from model import Point
from pie import Pie


def main():
    points = console_io.get_number_of_points()
    pie = Pie(Point(50, 50), 90, 50)
    lines = []
    for index in range(points):
        lines.append(console_io.read_line())

    index = 0
    for line in lines:
        index += 1
        percent, x, y = list(map(lambda l: int(l), line.split(' ')))
        is_inside = pie.is_inside(Point(x, y), percent)
        color = 'black' if is_inside else 'white'
        console_io.show_result(index, color)


if __name__ == '__main__':
    main()
