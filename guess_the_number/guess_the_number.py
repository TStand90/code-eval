import sys
import math


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            inputs = line.strip().split(' ')
            
            lower_bound = 0
            upper_bound = int(inputs[0])
            guess = math.ceil(upper_bound / 2)

            for answer in inputs[1:]:
                if answer == 'Yay!':
                    print(guess)
                elif answer == 'Lower':
                    upper_bound = guess - 1
                    guess = int(math.ceil(guess - ((upper_bound - lower_bound) // 2) - 1))
                elif answer == 'Higher':
                    lower_bound = guess + 1
                    guess = int(math.ceil(guess + ((upper_bound - lower_bound) // 2) + 1))


if __name__ == '__main__':
    main(sys.argv[1])