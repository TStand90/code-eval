import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            list_1, list_2 = line.split('|')

            list_1 = list_1.strip().split(' ')
            list_2 = list_2.strip().split(' ')

            multiplied_list = []
            for x, number in enumerate(list_1):
                multiplied_list.append(int(number) * int(list_2[x]))
            
            for element in multiplied_list:
                print('%d ' % element),

            print('')

if __name__ == '__main__':
    main(sys.argv[1])
