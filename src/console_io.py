def get_number_of_points():
    number_of_points = input()
    return int(number_of_points)


def read_line():
    line = input()
    values = line.split(' ')
    if len(values) != 3:
        raise Exception(f"Invalid input: {line}")

    return line


def show_result(number, color):
    print(f'Case #{number}: {color}')
