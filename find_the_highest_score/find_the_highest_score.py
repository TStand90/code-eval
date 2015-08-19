import sys


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            group_of_scores = line.strip().split(' | ')

            highest_scores = [None for x in range(len(group_of_scores[0].split(' ')))]
            for persons_scores in group_of_scores:
                for x, individual_score in enumerate(persons_scores.split(' ')):
                    if highest_scores[x] is None:
                        highest_scores[x] = int(individual_score)
                    else:
                        if highest_scores[x] < int(individual_score):
                            highest_scores[x] = int(individual_score)

            print(' '.join(map(str, highest_scores)))
              

            


if __name__ == '__main__':
    main(sys.argv[1])
