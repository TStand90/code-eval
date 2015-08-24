import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            dollar_amount = int(line.rstrip())
            text_amount = ''

            if dollar_amount == 0:
                print('ZeroDollar')
            else:
                text_amount += get_billion(dollar_amount)
                text_amount += get_million(dollar_amount)
                text_amount += get_thousands(dollar_amount)
                text_amount += get_hundreds(dollar_amount)

                if text_amount:
                    print(text_amount + 'Dollars')


def get_billion(amount):
    billion_amount = get_string_of_number(amount // 1000000000)

    if billion_amount:
        return billion_amount + 'Billion'
    else:
        return billion_amount


def get_million(amount):
    million_amount = ''

    hundreds_place = amount // 100000000
    tens_place = (amount // 1000000) % 100
    ones_place = amount // 1000000

    million_amount += get_hundreds_place(hundreds_place)
    million_amount += get_tens_place(tens_place)

    if tens_place not in range(10, 20):
        million_amount += get_ones_place(ones_place)

    if million_amount:
        million_amount += 'Million'

    return million_amount


def get_thousands(amount):
    thousands_amount = ''

    hundreds_place = amount // 100000
    tens_place = (amount // 1000) % 100
    ones_place = amount // 1000

    thousands_amount += get_hundreds_place(hundreds_place)
    thousands_amount += get_tens_place(tens_place)
    if tens_place not in range(10, 20):
        thousands_amount += get_ones_place(ones_place)

    if thousands_amount:
        thousands_amount += 'Thousand'

    return thousands_amount


def get_hundreds(amount):
    hundreds_amount = ''

    hundreds_place = amount // 100
    tens_place = (amount % 100)
    ones_place = amount

    hundreds_amount += get_hundreds_place(hundreds_place)
    hundreds_amount += get_tens_place(tens_place)
    if tens_place not in range(10, 20):
        hundreds_amount += get_ones_place(ones_place)

    return hundreds_amount


def get_ones_place(number):
    return get_string_of_number(number)


def get_tens_place(number):
    return get_tens_string_of_number(number)


def get_hundreds_place(number):
    number_string = get_string_of_number(number)

    if number_string:
        return number_string + 'Hundred'
    else:
        return ''


def get_string_of_number(number):
    if (number % 10) == 1:
        return 'One'
    elif (number % 10) == 2:
        return 'Two'
    elif (number % 10) == 3:
        return 'Three'
    elif (number % 10) == 4:
        return 'Four'
    elif (number % 10) == 5:
        return 'Five'
    elif (number % 10) == 6:
        return 'Six'
    elif (number % 10) == 7:
        return 'Seven'
    elif (number % 10) == 8:
        return 'Eight'
    elif (number % 10) == 9:
        return 'Nine'
    else:
        return ''


def get_tens_string_of_number(number):
    if number == 10:
        return 'Ten'
    elif number == 11:
        return 'Eleven'
    elif number == 12:
        return 'Twelve'
    elif number == 13:
        return 'Thirteen'
    elif number == 14:
        return 'Fourteen'
    elif number == 15:
        return 'Fifteen'
    elif number == 16:
        return 'Sixteen'
    elif number == 17:
        return 'Seventeen'
    elif number == 18:
        return 'Eighteen'
    elif number == 19:
        return 'Nineteen'
    elif ((number // 10) % 10) == 2:
        return 'Twenty'
    elif ((number // 10) % 10) == 3:
        return 'Thirty'
    elif ((number // 10) % 10) == 4:
        return 'Forty'
    elif ((number // 10) % 10) == 5:
        return 'Fifty'
    elif ((number // 10) % 10) == 6:
        return 'Sixty'
    elif ((number // 10) % 10) == 7:
        return 'Seventy'
    elif ((number // 10) % 10) == 8:
        return 'Eighty'
    elif ((number // 10) % 10) == 9:
        return 'Ninety'
    else:
        return ''


if __name__ == '__main__':
    main(sys.argv[1])

