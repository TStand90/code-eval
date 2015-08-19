import sys


def main(file_arg):
    with open(file_arg, 'r') as f:
        for line in f:
            line = line.rstrip()
            number_of_doors, iterations = line.split(' ')

            number_of_doors = int(number_of_doors)
            iterations = int(iterations)

            doors = [True] * number_of_doors


            for iteration in range(iterations - 1):
                doors = first_beat(doors)
                doors = second_beat(doors)

            doors = last_beat(doors)

            number_of_open_doors = 0

            for door in doors:
                if door:
                    number_of_open_doors += 1

            print(number_of_open_doors)


def first_beat(doors):
    for x, door in enumerate(doors):
        if (x + 1) % 2 == 0:
            doors[x] = False

    return doors


def second_beat(doors):
    for x, door in enumerate(doors):
        if (x + 1) % 3 == 0:
            if doors[x]:
                doors[x] = False
            else:
                doors[x] = True

    return doors


def last_beat(doors):
    if doors[-1]:
        doors[-1] = False
    else:
        doors[-1] = True

    return doors


if __name__ == '__main__':
    main(sys.argv[1])
