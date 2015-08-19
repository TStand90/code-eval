#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

bool prime_finder(int number);

int main(int argc, char *argv[])
{
    int sum_of_primes = 2;
	int x = 3;
	int primes_counter = 2;

	while (primes_counter <= 1000)
	{
	    if (prime_finder(x))
		{
	        sum_of_primes += x;
			primes_counter++;
		}
		x++;
	}

	cout << sum_of_primes << endl;

	return 0;
}

bool prime_finder(int number)
{
    for (int i = 2; i < number; i++)
	{
	    if (number % i == 0)
		{
		    return false;
		}
	}
	return true;
}
