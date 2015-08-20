import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            lcd, number_to_display = line.strip().split(';')

            lcd_list = [x for x in lcd.split(' ')]

            possible_numbers = []

            for each_number_lcd in lcd_list:
                possible_numbers.append(get_displayable_numbers(list(each_number_lcd)))

            number_to_display_list = list(number_to_display)

            # Get rid of the decimal in the list and append it to the previous
            # element

            decimal_index = number_to_display_list.index('.')
            number_to_display_list[decimal_index-1] = number_to_display_list[decimal_index-1] + '.'
            del(number_to_display_list[decimal_index])

            can_display = False

            while(possible_numbers):
                if number_can_be_displayed(number_to_display_list, possible_numbers):
                    break
                else:
                    possible_numbers = possible_numbers[1:]

            else:
                can_display = True

            if can_display:
                print('1')
            else:
                print('0')
            

def get_displayable_numbers(lcd_bits):
    '''
    Given the binary representation of broken and working LCD lights,
    return a list of numbers that can be displayed on that space.
    '''

    possible_numbers = []

    if lcd_bits[1] == '1' and lcd_bits[2] == '1':
        possible_numbers.append('1')
        if lcd_bits[7] == '1':
            possible_numbers.append('1.')

    if lcd_bits[0] == '1' and lcd_bits[1] == '1' and lcd_bits[3] == '1' and lcd_bits[4] == '1' and lcd_bits[6] == '1':
        possible_numbers.append('2')
        if lcd_bits[7] == '1':
            possible_numbers.append('2.')

    if lcd_bits[0] == '1' and lcd_bits[1] == '1' and lcd_bits[2] == '1' and lcd_bits[3] == '1' and lcd_bits[6] == '1':
        possible_numbers.append('3')
        if lcd_bits[7] == '1':
            possible_numbers.append('3.')

    if lcd_bits[1] == '1' and lcd_bits[2] == '1' and lcd_bits[5] == '1' and lcd_bits[6] == '1':
        possible_numbers.append('4')
        if lcd_bits[7] == '1':
            possible_numbers.append('4.')

    if lcd_bits[0] == '1' and lcd_bits[2] == '1' and lcd_bits[3] == '1' and lcd_bits[5] == '1' and lcd_bits[6] == '1':
        possible_numbers.append('5')
        if lcd_bits[7] == '1':
            possible_numbers.append('5.')

    if lcd_bits[0] == '1' and lcd_bits[2] == '1' and lcd_bits[3] == '1' and lcd_bits[4] == '1' and lcd_bits[5] == '1' and lcd_bits[6] == '1':
        possible_numbers.append('6')
        if lcd_bits[7] == '1':
            possible_numbers.append('6.')

    if lcd_bits[0] == '1' and lcd_bits[1] == '1' and lcd_bits[2] == '1':
        possible_numbers.append('7')
        if lcd_bits[7] == '1':
            possible_numbers.append('7.')

    if lcd_bits[0] == '1' and lcd_bits[1] == '1' and lcd_bits[2] == '1' and lcd_bits[3] == '1' and lcd_bits[4] == '1' and lcd_bits[5] == '1' and lcd_bits[6] == 1:
        possible_numbers.append('8')
        if lcd_bits[7] == '1':
            possible_numbers.append('8.')

    if lcd_bits[0] == '1' and lcd_bits[1] == '1' and lcd_bits[2] == '1' and lcd_bits[3] == '1' and lcd_bits[5] == '1' and lcd_bits[6] == 1:
        possible_numbers.append('9')
        if lcd_bits[7] == '1':
            possible_numbers.append('9.')

    if lcd_bits[0] == '1' and lcd_bits[1] == '1' and lcd_bits[2] == '1' and lcd_bits[3] == '1' and lcd_bits[4] == '1' and lcd_bits[5] == '1':
        possible_numbers.append('0')
        if lcd_bits[7] == '1':
            possible_numbers.append('0.')

    return possible_numbers
 

def number_can_be_displayed(number, display):
    if len(number) == 0:
        return True

    for possibility in display:
        if number[0] in possibility:
            number_can_be_displayed(number[1:], display[1:])
        else:
            return False

    return True


if __name__ == '__main__':
    main(sys.argv[1])
