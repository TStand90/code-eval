import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            stack = [int(number) for number in line.strip().split(' ')]

            print(' '.join(str(x) for x in stack[::-2]))


if __name__ == '__main__':
    main(sys.argv[1])