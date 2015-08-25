import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            coordinates = line.strip().replace('(', '').replace(')', '').split(', ')
            coordinates = [coordinate.split(',') for coordinate in coordinates]

            final_coordinates = []

            for coordinate in coordinates:
                final_coordinates.append((int(coordinate[0]), int(coordinate[1])))

            southwest, northwest, southeast, northeast = sorted(final_coordinates)

            if is_square(southwest, northwest, southeast, northeast):
                print("true")
            else:
                print("false")


def is_square(southwest, northwest, southeast, northeast):
    distance = southeast[0] - southwest[0]

    if northwest[1] - southwest[1] != distance:
        return False
    elif northeast[0] - northwest[0] != distance:
        return False
    elif northeast[1] - southeast[1] != distance:
        return False

    return True


if __name__ == '__main__':
    main(sys.argv[1])
