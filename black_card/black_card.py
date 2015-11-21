import sys


def main(file_arg):
	with open(file_arg) as f:
		for line in f:
			players, turns = line.strip().split(' | ')
			players = players.split(' ')
			turns = int(turns)
			turns = turns - 1

			while (len(players) > 1):
				eliminate_players(players, turns)

			print(players[0])


def eliminate_players(players, turns):
	while (turns >= len(players)):
		turns = turns - len(players)

	del(players[turns])
	return players


if __name__ == '__main__':
	main(sys.argv[1])