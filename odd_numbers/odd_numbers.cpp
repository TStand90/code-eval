#include <iostream>

int main(int argc, char *argv[])
{
    for(int i = 1; i < 100; i++)
    {
        if (i % 2 == 1)
        {
            std::cout << i << std::endl;
        }
    }
}