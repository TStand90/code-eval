#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
	char *pch;

    while (fgets(line, 1024, file)) {
	    pch = strtok (line, " ");
        int fizz = atoi(pch);

		pch = strtok (NULL, " ");
		int buzz = atoi(pch);

		pch = strtok (NULL, " ");
		int counter = atoi(pch);

		int i;

		for (i = 1; i <= counter; i++)
		{
		    if (i % fizz == 0 && i % buzz == 0) { printf("FB "); }
			else if (i % fizz == 0) { printf("F "); }
			else if (i % buzz == 0) { printf("B "); }
			else { printf("%i ", i); }
		}

        printf("\n");
    }

    return 0;
}
