import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            numbers = [int(number) for number in line.strip().split(',')]

            unique_numbers = set(numbers)

            for number in unique_numbers:
                if numbers.count(number) >= len(numbers) / 2:
                    print(number)
                    break
            else:
                print("None")


if __name__ == '__main__':
    main(sys.argv[1])
