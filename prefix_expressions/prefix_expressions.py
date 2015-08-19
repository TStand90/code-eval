import sys

OPERATORS = ['+', '*', '/']

def main(fileArg):
    with open(fileArg, 'r') as f:
        for line in f:
            expression = line.rstrip()
            tokens = expression.split(' ')

            for i, token in enumerate(tokens):
                if token not in OPERATORS:
                    tokens[i] = int(token)

            result = evaluate_expression(tokens)
            print(result[0])


def evaluate_expression(tokens):
    for eachToken in tokens:
        if eachToken in OPERATORS:
            tokens = [tokens[0]] + evaluate_expression(tokens[1:])

        if eachToken == '+':
            newToken = [tokens[1] + tokens[2]]
            tokens = newToken + tokens[3:]
        elif eachToken == '*':
            newToken = [tokens[1] * tokens[2]]
            tokens = newToken + tokens[3:]
        elif eachToken == '/':
            newToken = [tokens[1] // tokens[2]]
            tokens = newToken + tokens[3:]

        return tokens


if __name__ == '__main__':
    main(sys.argv[1])

