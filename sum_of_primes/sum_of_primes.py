def main():
    sum_of_primes = 2
    x = 3
    primes_counter = 2
    while (primes_counter <= 1000):
        if prime_finder(x):
            sum_of_primes += x
            primes_counter += 1
        x += 1

    print(sum_of_primes)


def prime_finder(number):
    for y in range(2, number):
        if (number % y == 0):
            return False
    return True


if __name__ == '__main__':
    main()
