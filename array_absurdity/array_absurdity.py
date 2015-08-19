import sys


def main(file_arg):
    with open(file_arg, 'r') as f:
        for line in f:
            line = line.rstrip()
            array_count, array = line.split(';')

            array = array.split(',')

            array = [int(x) for x in array]

            sorted_array = sorted(array)

            for i in range(len(sorted_array) - 1):
                if sorted_array[i] == sorted_array[i+1]:
                    duplicate = i
                    break
                    
            print(duplicate)


if __name__ == '__main__':
    main(sys.argv[1])
