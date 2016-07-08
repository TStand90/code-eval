#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> &split(const string &s, char delimiter, vector<string> &elements)
{
    stringstream ss(s);
    string item;

    while (getline(ss, item, delimiter)) {
        elements.push_back(item);
    }

    return elements;
}

vector<string> split(const string &s, char delimiter)
{
    vector<string> elements;
    split(s, delimiter, elements);

    return elements;
}

int main(int argc, char *argv[])
{
    ifstream file(argv[1]);
    string line;

    while(getline(file, line))
    {
        string output_line;
        vector<string> words = split(line, ' ');

        for (string word: words)
        {
            output_line += word[word.size() - 1];
            output_line += word.substr(1, word.size() - 2);
            output_line += word[0];
            output_line += ' ';
        }

        cout << output_line << endl;
    }
}
