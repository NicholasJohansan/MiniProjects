
# Robot War Game made by Nicholas Johansan
# Inspiration/Guidance from https://homepages.math.uic.edu/~lenz/f15.m260/project2.html
# Excluded the MedicRobot part

import os
import random

game_running = False

'''
Simplified 3x3 board for reference
col_no = x
row_no = total_rows-1-y
	  (0, 0)(0, 1)(0, 2)
(0, 0)[0, 2][1, 2][2, 2](0, 2)
(1, 0)[0, 1][1, 1][2, 1](1, 2)
(2, 0)[0, 0][1, 0][2, 0](2, 2)
	  (2, 0)(2, 1)(2, 2)
'''

class Robot():

	def __init__(self, team, x, y, direction, hp):
		self.team = team
		self.x = x
		self.y = y
		self.direction = direction
		self.hp = hp

	def get_team(self):
		return self.team
	def get_health(self):
		return self.hp
	def get_direction(self):
		return self.direction

	def left90(self, direction):
		return {
			"N":"W",
			"W":"S",
			"S":"E",
			"E":"N"
		}.get(direction)

	def right90(self, direction):
		return {
			'N':"E",
			"E":"S",
			"S":"W",
			"W":"N"
		}.get(direction)

	def healthchange(self, world, hp):
		self.hp += hp
		if self.hp < 0: world.kill_robot(self.x, self.y)
		if self.hp > 50: self.hp = 50

	def get_next_pos(self, direction):
		return {
			"N":(self.x, self.y+1),
			"S":(self.x, self.y-1),
			"E":(self.x+1, self.y),
			"W":(self.x-1, self.y)
		}.get(direction)

	def forward(self, world):
		x, y = self.get_next_pos(self.direction)
		if (x > -1 and x < world.row) and (y > -1 and y < world.row):
			if world.test_pos(x, y):
				return False
			world.move_robot(self.x, self.y, x, y)
			self.x = x
			self.y = y
			return True
		else:
			self.direction = self.left90(self.direction)
			self.direction = self.left90(self.direction)
			return True

class AttackRobot(Robot):

	def __init__(self, team, x, y, direction, hp):
		Robot.__init__(self, team, x, y, direction, hp)

	def test_enemy(self, world, x, y):
		if world.test_pos(x, y).team == self.team:
			return False
		else:
			return True

	def run_turn(self, world):
		#check forward
		x, y = Robot.get_next_pos(self, self.direction)
		if (x > -1 and x < world.row) and (y > -1 and y < world.row):
			if world.test_pos(x, y):
				if self.test_enemy(world, x, y):
					world.test_pos(x, y).healthchange(world, -random.randint(1,6))
					return
		#check right
		x, y = Robot.get_next_pos(self, Robot.right90(self, self.direction))
		if (x > -1 and x < world.row) and (y > -1 and y < world.row):
			if world.test_pos(x, y):
				if self.test_enemy(world, x, y):
					self.direction = Robot.right90(self, self.direction)
					return
		#check left
		x, y = Robot.get_next_pos(self, Robot.left90(self, self.direction))
		if (x > -1 and x < world.row) and (y > -1 and y < world.row):
			if world.test_pos(x, y):
				if self.test_enemy(world, x, y):
					self.direction = Robot.left90(self, self.direction)
					return
		#random move
		randmove = random.choice(["F", "F", "L", "R"])
		if randmove == "F":
			Robot.forward(self, world)
		elif randmove == "L":
			self.direction = Robot.left90(self, self.direction)
		else:
			self.direction = Robot.right90(self, self.direction)
		return

class World():

	def __init__(self, size):
		self.row = size
		self.col = self.row
		self.board = []
		for row in range(self.row):
			self.board.append([])
			for col in range(self.col):
				self.board[row].append(None)

	def kill_robot(self, x, y):
		col, row = x, self.row-1-y
		self.board[row][col] = None

	def test_pos(self, x, y):
		col, row = x, self.row-1-y
		if self.board[row][col]: return self.board[row][col] 
		return None

	def add_attack_robot(self, team, x, y, direction):
		col, row = x, self.row-1-y
		self.board[row][col] = AttackRobot(team, x, y, direction, 50) #50 HP

	#def add_medic_robot(self, team, x, y, direction):
	#	col, row = x, self.row-1-y
	#	self.board[row][col] = MedicRobot(team, x, y, direction, 50) #50 HP

	def move_robot(self, oldx, oldy, newx, newy):
		oldcol, oldrow, newcol, newrow = oldx, self.row-1-oldy, newx, self.row-1-newy
		self.board[oldrow][oldcol], self.board[newrow][newcol] = None, self.board[oldrow][oldcol]

	def run_turn(self):
		for row in range(self.row):
			for col in range(self.col):
				if self.board[row][col]:
					self.board[row][col].run_turn(self)

	def game_over(self):
		team1 = 0
		team2 = 0
		winner = None
		for row in range(self.row):
			for col in range(self.col):
				if self.board[row][col]:
					if self.board[row][col].team == 1:
						team1 += 1
					elif self.board[row][col].team == 2:
						team2 += 1
		if team1 == 0:
			winner = 2
		elif team2 == 0:
			winner = 1
		return winner

	def team_count(self):
		team1 = 0
		team2 = 0
		for row in range(self.row):
			for col in range(self.col):
				if self.board[row][col]:
					if self.board[row][col].team == 1:
						team1 += 1
					elif self.board[row][col].team == 2:
						team2 += 1
		return team1, team2

def print_world(world):
	print("-" * 60)
	print("Robot Legend - [A50N, a50E]\nIf the first letter is capital, it is Team1, else, it is Team2!\nThe middle 2 digits are the health! Robots start with 50 HP!\nThe last letter stands for its direction! N - North, E - East, S - South, W - West!")
	print("-" * 60)
	for y in range(world.row-1, -1, -1):
		line = ""
		for x in range(0, world.row):
			r = world.test_pos(x, y)
			if not r:
				line += ".... "
			else:
				if isinstance(r, AttackRobot):
					rtype = "A"
				else:
					rtype = "!"
				if r.get_team() == 1:
					line += "%s%02i%s " % (rtype, r.get_health(), r.get_direction())
				else:
					line += "%s%02i%s " % (rtype.lower(), r.get_health(), r.get_direction())
		print(line)
	print("-" * 60)
	team1, team2 = world.team_count()
	print(f"{team1} Team 1 Robots left\n{team2} Team 2 Robots left")
	print("-" * 60)
	print("Press [Enter] to Continue")

def response_handler(thing):
	if thing == "size":
		res = input("What size would you like the world to be?\nThe world will be the [number] you entered will be received in [number]x[number] size.\nFor e.g. if 5 is entered, the world is 5x5!\nEnter your number\n>> ")
		try:
			res = int(res)
			return res
		except ValueError:
			os.system('cls')
			print("You didn't enter a number! Try again!")
			return response_handler('size')
	elif thing == "team1":
		res = input("How many robots do you want in Team 1?\nEnter the amount of robots in Team 1!\n>> ")
		try:
			res = int(res)
			return res
		except ValueError:
			os.system('cls')
			print("You didn't enter a number! Try again!")
			return response_handler('team1')
	elif thing == "team2":
		res = input("How many robots do you want in Team 2?\nEnter the amount of robots in Team 2!\n>> ")
		try:
			res = int(res)
			return res
		except ValueError:
			os.system('cls')
			print("You didn't enter a number! Try again!")
			return response_handler('team2')

def addRobot(team, world, occupied):
	x = random.randrange(0, world.row)
	y = random.randrange(0, world.row)
	direction = random.choice(["N","E","S","W"])
	if (x, y) in occupied:
		addRobot(team, world, occupied)
		return
	world.add_attack_robot(team, x, y, direction)
	occupied.append((x, y))
	return

def runGame(world):
	global game_running
	while game_running:
		input()
		os.system('cls')
		print_world(world)
		world.run_turn()
		if world.game_over():
			input(f"Team {world.game_over()} won!\nGame Ended!\nExit the game by quitting the program or Play Again!\nTo play again, press Enter!\n")
			game_running = False
			main()

def main():
	global game_running
	input("Welcome to\nTotally Inaccurate Robot Warfare Simulator [TIRWS]\nPress Enter to Play!\n")
	size = response_handler("size")
	os.system('cls')
	team1no = response_handler('team1')
	os.system('cls')
	team2no = response_handler('team2')
	os.system('cls')
	print("Setting Up World...")
	world = World(size)
	occupied = []
	full = False
	for i in range(team1no):
		if len(occupied) == (world.row)**2:
			full = True
			break
		addRobot(1, world, occupied)
	for i in range(team2no):
		if len(occupied) == (world.row)**2:
			full = True
			break
		addRobot(2, world, occupied)
	if full:
		print("The game have done setting up, but\nThere are more robots than space available!\nRestart the game or continue at your own risk!\nEnter to continue or close the program to restart!\n")
	else:
		print("The game have done setting up!\nPress Enter when you are ready!\n")
	game_running = True
	runGame(world)

main()