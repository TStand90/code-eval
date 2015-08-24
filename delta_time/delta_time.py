import sys
from datetime import datetime


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            timeString1, timeString2 = line.strip().split(' ')

            time1 = datetime.strptime(timeString1, "%H:%M:%S")
            time2 = datetime.strptime(timeString2, "%H:%M:%S")

            if time1 > time2:
                difference = time1 - time2
            else:
                difference = time2 - time1

            seconds = difference.seconds % 60
            hours = difference.seconds // 3600
            minutes = difference.seconds % 3600 // 60

            print("%02d:%02d:%02d" % (hours, minutes, seconds))


if __name__ == '__main__':
    main(sys.argv[1])
