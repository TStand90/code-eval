#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream file(argv[1]);
    string line;

    while(getline(file, line))
    {
        istringstream iss(line);

        int i;
        std::vector<int> vect;

        while(iss >> i)
        {
            vect.push_back(i);

            if(iss.peek() == ',')
                iss.ignore();   
        }

        int quotient = vect[0] / vect[1];
        int remainder = vect[0] - (vect[1] * quotient);

        cout << remainder << endl;
    }

    return 0;
}