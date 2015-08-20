import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            numbers, wanted_sum = line.strip().split(';')

            numbers_list = [int(number) for number in numbers.split(',')]
            wanted_sum = int(wanted_sum)

            number_pairs = []

            for x, each_number in enumerate(numbers_list):
                result = find_pair(each_number, numbers_list[x+1:], wanted_sum)
                if result:
                    number_pairs.append(result)

            result_list = []

            for each_pair in number_pairs:
                result_list.append("%s,%s" % (each_pair[0], each_pair[1]))

            if result_list:
                print(';'.join(result_list))
            else:
                print('NULL')


def find_pair(number, remaining_list, wanted_sum):
    if number >= wanted_sum:
        return None

    for each_remaining_number in remaining_list:
        if number + each_remaining_number == wanted_sum:
            return (number, each_remaining_number)


if __name__ == '__main__':
    main(sys.argv[1])