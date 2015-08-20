import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            length, characters = line.strip().split(',')
            length = int(length)

            unique_characters = []

            for character in characters:
                if character not in unique_characters:
                    unique_characters.append(character)

            string_list = get_words(length, unique_characters)

            string_list = sorted(string_list)

            print(','.join(string_list))


def get_words(length, alphabet, prefix=""):
    if len(prefix) == length:
        return [prefix]

    result = []
    for character in alphabet:
        local_result = get_words(length, alphabet, prefix + character)

        for x in local_result:
            result.append(x)

    return result


if __name__ == '__main__':
    main(sys.argv[1])
