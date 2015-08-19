#include <iostream>
#include <sstream>
#include <fstream>

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

		if (number % 2 == 0) { cout << "1" << endl;}
		else { cout << "0" << endl;}
	}

	return 0;
}
