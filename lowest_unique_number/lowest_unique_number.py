import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            numbers = line.strip().split(' ')

            numbers = [int(number) for number in numbers]
            sorted_numbers = sorted(numbers)

            unique_numbers = []

            for number in numbers:
                if numbers.count(number) == 1:
                    unique_numbers.append(number)

            if unique_numbers:
                print(numbers.index(min(unique_numbers)) + 1)
            else:
                print(0)


if __name__ == '__main__':
    main(sys.argv[1])