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
        int bit_counter = 0;
        
		for (int i = 0; i < bit_string.length(); i++)
		{
		    char c = bit_string[i];
			if (c == '1') { bit_counter++; }
		}

	    cout << bit_counter << endl;
	}

	return 0;
}
