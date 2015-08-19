import sys

def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            age = int(line.rstrip())

            age_categorizer(age)


def age_categorizer(age):
    if age in range(0, 3):
        print("Still in Mama's arms")
    elif age in range(3, 5):
        print("Preschool Maniac")
    elif age in range(5, 12):
        print("Elementary school")
    elif age in range(12, 15):
        print("Middle school")
    elif age in range(15, 19):
        print("High school")
    elif age in range(19, 23):
        print("College")
    elif age in range(23, 66):
        print("Working for the man")
    elif age in range(66, 101):
        print("The Golden Years")
    else:
        print("This program is for humans")
            

if __name__ == '__main__':
    main(sys.argv[1])
