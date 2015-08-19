#include <iostream>
#include <sstream>
#include <fstream>

int fibonacci(int number);

int main(int argc, char *argv[])
{
    using namespace std;

	ifstream file(argv[1]);
	int number;
	string line;

	while(getline(file, line))
	{
	    istringstream iss(line);
		iss >> number;

		cout << fibonacci(number) << endl;
	}

	return 0;
}

int fibonacci(int number)
{
    if (number == 1 || number == 2)
	{
	    return 1;
	}
	else if (number == 0)
	{
	    return 0;
	}
	else
	{
	    return fibonacci(number - 2) + fibonacci(number - 1);
	}
}
