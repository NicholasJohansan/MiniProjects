
# Tic Tac Toe written by Nicholas Johansan
# Part of practicing Object Oriented Programming

import random, os

cls = lambda: os.system('cls')

class TicTacToe:
	choices = [1,2,3,4,5,6,7,8,9]
	win_conditions = [
		(1, 2, 3),
		(4, 5, 6),
		(7, 8, 9),
		(1, 4, 7),
		(2, 5, 8),
		(3, 6, 9),
		(1, 5, 9),
		(7, 5, 3)
	]
	def __init__(self):
		self.taken = []
		self.player = []
		self.computer = []

	def spot_taken(self, spot):
		return spot in self.taken

	def get_free_spots(self):
		return list(filter(lambda p: not self.spot_taken(p), TicTacToe.choices))

	def no_more_spots(self):
		return self.taken == TicTacToe.choices

	def win_check(self):
		for plays, symbol in [(self.player, 'x'), (self.computer, 'o')]:
			for win_condition in TicTacToe.win_conditions:
				if all([pos in plays for pos in win_condition]): return symbol
		return None

	def draw_board(self):
		board = """
		|---|---|---|
		| 1 | 2 | 3 |
		|---|---|---|
		| 4 | 5 | 6 |
		|---|---|---|
		| 7 | 8 | 9 |
		|---|---|---|
		"""
		for x in self.player: board = board.replace(f"{x}", "x")
		for o in self.computer: board = board.replace(f"{o}", "o")
		return board

def main(first=True):
	if first: input("\nTic Tac Toe v0\nPress [Enter] to play!")
	else: input("\nTic Tac Toe v0\nPress [Enter] to play again!")
	cls()
	game = TicTacToe()
	while True:
		print(game.draw_board())
		pos = input(f"\n\rEnter the position in which you would like to place\nAvailable options: {', '.join(map(lambda p: str(p), game.get_free_spots()))}\nNote: You are playing as \'x\'\n>> ")
		cls()
		try: pos = int(pos)
		except ValueError:
			print(f"\rDoes position `{pos}` looks like any of the available options?")
			continue
		if pos not in TicTacToe.choices:
			print(f"\rDoes position `{pos}` looks like any of the available options?")
			continue
		if game.spot_taken(pos):
			print(f"\rPosition `{pos}` have already been taken, please choose an available spot!")
			continue

		game.taken.append(pos)
		game.player.append(pos)
		print(f"You chose position `{pos}`!")

		if game.win_check() == 'x':
			print(game.draw_board())
			print("You won!")
			break

		if game.no_more_spots() or not game.get_free_spots():
			print(game.draw_board())
			print("It\'s a tie!")
			break

		pc_pos = random.choice(game.get_free_spots())
		game.taken.append(pc_pos)
		game.computer.append(pc_pos)
		print(f"PC chose position `{pc_pos}`!")

		if game.win_check() == 'o':
			print(game.draw_board())
			print("You lost!")
			break

	return main(first=False)

if __name__ == '__main__':
	main()