nclude <iostream>
#include <fstream>
#include <cctype>
#include <locale>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream stream(argv[1]);
    string line;

    while (getline(stream, line))
    {
        locale loc;

        for (int i = 0; i < line.length(); i++) {
            cout << tolower(line[i], loc);
        }

        cout << endl;
    }

    return 0;
}
