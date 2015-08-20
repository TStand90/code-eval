import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            location_list = line.strip().split(';')

            location_list = [location.strip() for location in location_list if location]

            distances_from_start = []

            for each_location in location_list:
                name, distance = each_location.split(',')
                distances_from_start.append(int(distance))

            distances_from_start = sorted(distances_from_start)

            distances = []
            distances.append(distances_from_start[0])

            for i, distance in enumerate(distances_from_start[1:]):
                distances.append(distances_from_start[i+1] - distances_from_start[i])

            print(','.join([str(distance) for distance in distances]))


if __name__ == '__main__':
    main(sys.argv[1])
