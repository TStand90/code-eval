#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

vector<bool> first_beat(vector<bool> doors);
vector<bool> second_beat(vector<bool> doors);
vector<bool> last_beat(vector<bool> doors);

int main(int argc, char *argv[])
{
    ifstream file(argv[1]);
    string line;

    while(getline(file, line))
    {
        int number_of_doors;
        int iterations;

        istringstream iss(line);
        iss >> number_of_doors >> iterations;

        vector<bool> doors(number_of_doors, true);

        for (int i = 0; i < iterations - 1; i++)
        {
            doors = first_beat(doors);
            doors = second_beat(doors);
        }

        doors = last_beat(doors);

        int number_of_open_doors = count(doors.begin(), doors.end(), true);

        cout << number_of_open_doors << endl;
    }

    return 0;
}

vector<bool> first_beat(vector<bool> doors)
{
    for (int i = 0; i < doors.size(); i++)
    {
        if (((i + 1) % 2) == 0)
        {
            doors[i] = false;
        }
    }

    return doors;
}

vector<bool> second_beat(vector<bool> doors)
{
    for (int i = 0; i < doors.size(); i++)
    {
        if (((i + 1) % 3) == 0)
        {
            if (doors[i])
            {
                doors[i] = false;
            }
            else
            {
                doors[i] = true;
            }
        }
    }

    return doors;
}

vector<bool> last_beat(vector<bool> doors)
{
    int last_door_index = doors.size() - 1;

    if (doors[last_door_index])
    {
        doors[last_door_index] = false;
    }
    else
    {
        doors[last_door_index] = true;
    }

    return doors;
}
