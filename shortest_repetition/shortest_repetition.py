import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            line = line.strip()

            first_character = line[0]
            length = None

            for x, character in enumerate(line[1:]):
                if character == first_character:
                    length = x + 1
                    break
            else:
                length = len(line)

            print(length)


if __name__ == '__main__':
    main(sys.argv[1])