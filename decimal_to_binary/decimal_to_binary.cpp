#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>

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
		string bit_string = bitset<32>(number).to_string();

		while (bit_string[0] == '0')
		{
			bit_string.erase(0,1);
		}
        
	    cout << bit_string << endl;
	}

	return 0;
}
