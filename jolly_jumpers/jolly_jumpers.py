import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            n = int(line.strip().split(' ')[0])
            sequence = [int(x) for x in line.strip().split(' ')[1:]]

            difference_sequence = []

            while (len(sequence) > 1):
                sequence[0] = abs(sequence[0] - sequence[1])
                difference_sequence.append(sequence[0])
                del(sequence[0])

            for x in range(1, n):
                if x not in difference_sequence:
                    print("Not jolly")
                    break
            else:
                print("Jolly")


if __name__ == '__main__':
    main(sys.argv[1])
