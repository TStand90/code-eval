import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            numbers = line.strip().split(' ')

            numbers = [int(number) for number in numbers]

            previous_number = numbers[0]
            counter = 0
            compressed_sequence = []

            for number in numbers:
                if number != previous_number:
                    compressed_sequence.append(counter)
                    compressed_sequence.append(previous_number)
                    counter = 1
                    previous_number = number
                else:
                    counter += 1

            compressed_sequence.append(counter)
            compressed_sequence.append(previous_number)

            print(' '.join([str(number) for number in compressed_sequence]))


if __name__ == '__main__':
    main(sys.argv[1])