#include <stdio.h>
#include <string.h>

int prime_finder(int number);

int main(int argc, const char * argv[]) {

    int sum_of_primes = 2;
	int x = 3;
	int primes_counter = 2;

    while (primes_counter <= 1000) {
		if (prime_finder(x))
		{
			sum_of_primes += x;
            primes_counter++;
		}
		x++;
    }

	printf("%i\n", sum_of_primes);

    return 0;
}

int prime_finder(int number)
{
	int i;
    for (i = 2; i < number; i++)
	{
	    if (number % i == 0)
		{
		    return 0;
		}
	}
	return 1;
}
