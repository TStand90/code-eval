import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            n, days = line.strip().split(';')

            n = int(n)
            days = days.split(' ')
            days = [int(day) for day in days]

            ranges = []

            for x in range(len(days) - n + 1):
                ranges.append(days[x:x+n])

            sums = []

            for each_range in ranges:
                sums.append(sum(each_range))

            if max(sums) > 0:
                print(max(sums))
            else:
                print(0)


if __name__ == '__main__':
    main(sys.argv[1])
