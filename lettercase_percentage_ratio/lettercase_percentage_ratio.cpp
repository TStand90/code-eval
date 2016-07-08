#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream file(argv[1]);
    string line;

    while(getline(file, line))
    {
        int number_of_upper_case = 0;
        int number_of_lower_case = 0;
        int number_of_letters = line.length();

        for (int i = 0; i < line.length(); i++)
        {
            if (isupper(line[i]))
            {
                number_of_upper_case++;
            }
            else
            {
                number_of_lower_case++;
            }
        }

        std::cout << std::fixed;
        std::cout << std::setprecision(2);

        float upper_case_percentage = (float) number_of_upper_case / (float) number_of_letters * 100;
        float lower_case_percentage = (float) number_of_lower_case / (float) number_of_letters * 100;

        cout << "lowercase: " << lower_case_percentage << " uppercase: " << upper_case_percentage << endl;
    }

    return 0;
}
