import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            elements, swap_positions = line.strip().split(' : ')
            elements = [int(element) for element in elements.split(' ')]
            swap_positions = swap_positions.split(', ')
            swap_positions = [position.split('-') for position in swap_positions]

            swap_pairs = []

            for swap in swap_positions:
                position_pair = []
                for x in swap:
                    position_pair.append(int(x))

                swap_pairs.append(position_pair)
                
            for pair in swap_pairs:
                elements[pair[0]], elements[pair[1]] = elements[pair[1]], elements[pair[0]]
                
            print(' '.join([str(element) for element in elements]))


if __name__ == '__main__':
    main(sys.argv[1])
