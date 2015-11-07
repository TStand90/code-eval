import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            if line.rstrip() != '':
                split_line_reversed = line.rstrip().split(' ')[::-1]
                reversed_sentence = ' '.join(split_line_reversed)
                print(reversed_sentence)


if __name__ == '__main__':
    main(sys.argv[1])