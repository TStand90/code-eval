var upperLimit = 1000;

sum_of_primes(upperLimit)

function sum_of_primes(upperLimit) {
    var sumOfPrimes = 2;
    var x = 3;
    var primesCounter = 2;

    while (primesCounter <= upperLimit) {
        if (is_prime(x)) {
            sumOfPrimes += x;
            primesCounter++;
        }
        x++;
    }

    console.log(sumOfPrimes);
}

function is_prime(number) {
    for (var i = 2; i < number; i++) {
        if (number % i == 0) {
            return false;
        }
    }

    return true;
}