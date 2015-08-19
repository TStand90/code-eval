import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            number = int(line)
            print(fibo(number))

def fibo(number):
    if number == 1 or number == 2:
        return(1)
    elif number == 0:
        return(0)
    else:
        return(fibo(number - 2) + fibo(number-1))

if __name__ == '__main__':
    main(sys.argv[1])
