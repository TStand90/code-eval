import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            line = line.strip()

            tokens = list(line)

            if valid_parentheses(tokens):
                print("True")
            else:
                print("False")


def valid_parentheses(tokens):
    '''
    Given a set of tokens, determine of the parentheses are well formed.
    '''

    if len(tokens) % 2 == 1:
        # If there is an odd number of tokens, the parentheses cannot be
        # well formed.
        return False

    previous_tokens = []

    for token in tokens:
        if token in ['(', '{', '[']:
            previous_tokens.append(token)
        else:
            if previous_tokens:
                if (token == ')' and previous_tokens[-1] == '(') or (token == '}' and previous_tokens[-1] == '{') or (token == ']' and previous_tokens[-1] == '['):
                    del(previous_tokens[-1])
                else:
                    return False
            else:
                return False

    return True


if __name__ == '__main__':
    main(sys.argv[1])
