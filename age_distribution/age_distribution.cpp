#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char *argv[])
{
    using namespace std;

	ifstream file(argv[1]);
	int age;
	string line;

	while (getline(file, line))
	{
	    istringstream iss(line);
		iss >> age;

		if (age >= 0 && age < 3) { cout << "Still in Mama's arms" << endl; }
		else if (age >= 3 && age < 5) { cout << "Preschool Maniac" << endl; }
		else if (age >= 5 && age < 12) { cout << "Elementary school" << endl; }
		else if (age >= 12 && age < 15) { cout << "Middle school" << endl; }
		else if (age >= 15 && age < 19) { cout << "High school" << endl; }
		else if (age >= 19 && age < 23) { cout << "College" << endl; }
		else if (age >= 23 && age < 66) { cout << "Working for the man" << endl; }
		else if (age >= 66 && age < 101) { cout << "The Golden Years" << endl; }
		else { cout << "This program is for humans" << endl; }
	}

	return 0;
}
