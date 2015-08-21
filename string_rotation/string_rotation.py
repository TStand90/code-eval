import sys
import collections


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            word, rotated = line.strip().split(',')

            word = list(word)
            rotated = list(rotated)

            for x in range(len(rotated)):
                if rotate_list(rotated, x) == word:
                    print("True")
                    break
            else:
                print("False")


def rotate_list(list_to_rotate, amount):
    return list_to_rotate[-amount:] + list_to_rotate[:-amount]


if __name__ == '__main__':
    main(sys.argv[1])
