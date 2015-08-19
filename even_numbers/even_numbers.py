import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            number = int(line)
            if number % 2 == 0:
                print('1')
            else:
                print('0')



if __name__ == '__main__':
    main(sys.argv[1])
