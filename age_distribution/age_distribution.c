#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];

	int age;

    while (fgets(line, 1024, file)) {
        age = atoi(line);

		int i;

		if (age >= 0 && age < 3) { printf("Still in Mama's arms\n"); }
		else if (age >= 3 && age < 5) { printf("Preschool Maniac\n"); }
		else if (age >= 5 && age < 12) { printf("Elementary school\n"); }
		else if (age >= 12 && age < 15) { printf("Middle school\n"); }
		else if (age >= 15 && age < 19) { printf("High school\n"); }
		else if (age >= 19 && age < 23) { printf("College\n"); }
		else if (age >= 23 && age < 66) { printf("Working for the man\n"); }
		else if (age >= 66 && age < 101) { printf("The Golden Years\n"); }
		else { printf("This program is for humans\n"); }
    }

    return 0;
}
