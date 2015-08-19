import sys

TELEPHONE_WORDS = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def main(fileArg):
    with open(fileArg, 'r') as f:
        for line in f:
            telephoneNumber = line.rstrip()
            translated = []
            for eachNumber in telephoneNumber:
                translated.append(TELEPHONE_WORDS[eachNumber])
            
            finalList = []

            wholeList = iterate_through(translated, [], "")
            stringList = ','.join(wholeList)
            print(stringList)


def iterate_through(theList, wholeList, subString):
    if not theList:
        return None
    else:
        for eachElement in theList[0]:
            subString += eachElement

            if not iterate_through(theList[1:], wholeList, subString):
                wholeList.append(subString)

            subString = subString[:-1]

    return wholeList


if __name__ == '__main__':
    main(sys.argv[1])

