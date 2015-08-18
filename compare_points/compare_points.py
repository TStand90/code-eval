import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            O, P, Q, R = line.rstrip().split(' ')
            O = int(O)
            P = int(P)
            Q = int(Q)
            R = int(R)

            north = False
            south = False
            east = False
            west = False

            if (Q > O):
                east = True
            elif (Q < O):
                west = True

            if (P > R):
                south = True
            elif (P < R):
                north = True

            result = ''

            if (north):
                result += 'N'
            elif (south):
                result += 'S'

            if (east):
                result += 'E'
            elif (west):
                result += 'W'

            if not result:
                result = 'here'

            print(result)


if __name__ == '__main__':
    main(sys.argv[1])
