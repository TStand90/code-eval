#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main (int argc, char *argv[])
{
    ifstream file(argv[1]);
    string line;

    while(getline(file, line))
    {
        string output_line;

        for (int i = 0; i < line.length(); i++)
        {
            if (isupper(line[i]))
            {
                output_line += tolower(line[i]);
            }
            else
            {
                output_line += toupper(line[i]);
            }
        }

        cout << output_line << endl;
    }

    return 0;
}
