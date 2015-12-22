#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>

using namespace std;

int count_zeros(string binary_string);

int main(int argc, char *argv[])
{
    int desired_number_of_zeros;
    int upper_range;

    ifstream file(argv[1]);
    string line;

    while(getline(file, line))
    {
        istringstream iss(line);
        iss >> desired_number_of_zeros >> upper_range;

        int number_of_hits = 0;

        for (int i = 1; i <= upper_range; i++)
        {
            string binary_string = std::bitset<10>(i).to_string();

            // Get the number of zeros in the binary string
            int zero_count = count_zeros(binary_string);

            // Check if the number of zeros is what we're looking for
            if (zero_count == desired_number_of_zeros)
            {
                number_of_hits++;
            }
        }

        cout << number_of_hits << endl;
    }

    return 0;
}

int count_zeros(string binary_string)
{
    int zero_count = 0;

    // First, iterate until we hit a '1' (that is, ignore the preceeding zeros)
    int i = 0;

    while (i <= binary_string.length())
    {
        if (binary_string[i] == '1')
        {
            break;
        }

        i++;
    }

    // Now count the number of zeros
    for (i; i < binary_string.length(); i++)
    {
        if (binary_string[i] == '0')
        {
            zero_count++;
        }
    }

    return zero_count;
}