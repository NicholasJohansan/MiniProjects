
# Rock Paper Scissors written by Nicholas Johansan
# Part of practicing Object Oriented Programming

try:
	from enum import Enum
	import os, random
except ImportError:
	print(f"{','.join(ImportError.mro)} failed to import")

cls = lambda: os.system('cls')
class RPS(Enum):
	Paper = "Paper"
	Scissors = "Scissors"
	Rock = "Rock"

	@staticmethod
	def determine(pc, user):
		if (pc == RPS.Paper and user == RPS.Scissors) or (pc == RPS.Scissors and user == RPS.Rock) or (pc == RPS.Rock and user == RPS.Paper):
			return f"You chose {user.value} and the PC chose {pc.value}, you won!"
		elif (pc == RPS.Paper and user == RPS.Rock) or (pc == RPS.Scissors and user == RPS.Paper) or (pc == RPS.Rock and user == RPS.Scissors):
			return f"You chose {user.value} and the PC chose {pc.value}, you lost!"
		elif (pc == user):
			return f"You chose {user.value} and the PC chose {pc.value}, it was a tie!"

def main():
	while True:
		cls()
		user_choice = input("Key in your choice\n>> ")
		cls()
		user_choice = RPS._value2member_map_.get(user_choice)
		pc = random.choice([RPS.Rock, RPS.Paper, RPS.Scissors])
		if not user_choice:
			print(f"{user_choice} isn\'t any of the following:\n{','.join(RPS._value2member_map_.keys())}")
			input("Enter to try again!")
			continue
		print(RPS.determine(pc, user_choice))
		input("Enter to play another game!")

if __name__ == '__main__':
	main()

