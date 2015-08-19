#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char *argv[])
{
    using namespace std;

    ifstream file(argv[1]);
    int fizz, buzz, count;
    string line;

    while(getline(file, line))
    {
        istringstream iss(line);
        iss >> fizz >> buzz >> count;

        for (int i = 1; i <= count; i++)
        {
            if (i % fizz == 0 && i % buzz == 0) { cout << "FB "; }
            else if (i % fizz == 0) { cout << "F "; }
            else if (i % buzz == 0) { cout << "B "; }
            else { cout << i << " "; }
        }
        
        cout << endl;
    }

    return 0;
}
