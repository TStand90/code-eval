#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char *argv[])
{
    using namespace std;

	ifstream file(argv[1]);
	int number;
	string line;

	int sum = 0;

	while(getline(file, line))
	{
	    istringstream iss(line);
		iss >> number;

		sum += number;
	}

	cout << sum << endl;

	return 0;
}
