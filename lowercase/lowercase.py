import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            print(line.rstrip().lower())


if __name__ == '__main__':
    main(sys.argv[1])
