
# Hangman written by Nicholas Johansan

import random, os

pics = ['''
	 +---+
			 |
			 |
			 |
			===''', '''
	 +---+
	 O   |
			 |
			 |
			===''', '''
	 +---+
	 O   |
	 |   |
			 |
			===''', '''
	 +---+
	 O   |
	/|   |
			 |
			===''', '''
	 +---+
	 O   |
	/|\  |
			 |
			===''', '''
	 +---+
	 O   |
	/|\  |
	/    |
			===''', '''
	 +---+
	 O   |
	/|\  |
	/ \  |
			===''', '''
		+---+
	 [O   |
	 /|\  |
	 / \  |
			 ===''', '''
		+---+
	 [O]  |
	 /|\  |
	 / \  |
			 ===''']
HANGMAN_PICS = pics

difficulty = 'X'
words = {
	'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
	'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
	'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
	'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()
}

def hangmanGenerateWord(wordDict):
	wordKey = random.choice(list(wordDict.keys()))
	wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
	return [wordDict[wordKey][wordIndex], wordKey]

def hangmanGraphics(missedLetters, correctLetters, word):
	print(f"\r\n{HANGMAN_PICS[len(missedLetters)]}")
	print(f"\r\nMissed Letters:", end=" ")
	for letter in missedLetters:
		print(f"{letter}", end=" ")
	blanks = "_" * len(word)
	for i in range(len(word)):
		if word[i] in correctLetters:
			blanks = blanks[:i] + word[i] + blanks[i+1:]
	hangmanMsg = "\nWord: "
	for letter in blanks:
		hangmanMsg += f"{letter} "
	print(hangmanMsg)

def hangmanGuess(alreadyGuessed):
	while True:
		guess = input("\r\nGuess a letter.\n>>> ").lower()
		if len(guess) != 1:
			print("\r\nPlease enter a single letter.")
		elif guess in alreadyGuessed:
			print("\r\nYou have already guessed that letter.\nChoose again.")
		elif guess not in "abcdefghijklmnopqrstuvwxyz":
			print("\r\nPlease enter a letter.")
		else:
			return guess

def hangmanWin(gameRunning, word):
	userInput = input(f"\r\nCongrats!\nThe word was {word}.\nYou won!\nPlay again? Yes or No\n>>> ").lower()
	if userInput in ["yes", "no"]:
		if userInput == "yes":
			hangmanGame()
		elif userInput == "no":
			gameRunning = False
			hangmanGame()
	else:
		os.system('cls')
		print("\r\nHangman")
		print(f"\r\nYou entered neither yes nor no.\nTry again.")
		hangmanWin(gameRunning, word)

def hangmanLose(gameRunning, word):
	userInput = input(f"\r\nThe word was {word}.\nYou lost!\nPlay again? Yes or No\n>>> ").lower()
	if userInput in ["yes", "no"]:
		if userInput == "yes":
			hangmanGame()
		elif userInput == "no":
			gameRunning = False
			hangmanGame()
	else:
		os.system('cls')
		print("\r\nHangman")
		print(f"\r\nYou entered neither yes nor no.\nTry again.")
		hangmanLose(gameRunning, word)

def hangmanDifficulty():
	global difficulty
	difficulty = 'X'
	difficulty = input("\r\nEnter Difficulty:\nE - Easy, M- Medium, H - Hard.\n>>> ").upper()
	if difficulty not in ['E', 'M', 'H']:
		os.system('cls')
		print("\r\nHangman")
		print(f"\r\n{difficulty} is neither E nor M nor H.\nTry again.")
		hangmanDifficulty()
	elif difficulty == 'M':
		del HANGMAN_PICS[8]
		del HANGMAN_PICS[7]
	elif difficulty == 'H':
		del HANGMAN_PICS[8]
		del HANGMAN_PICS[7]
		del HANGMAN_PICS[5]
		del HANGMAN_PICS[3]

def hangmanReset():
	global HANGMAN_PICS
	HANGMAN_PICS = pics

def hangmanGame():
	os.system('cls')
	wordset = ''
	hangmanReset()
	print("\r\nHangman")
	hangmanDifficulty()
	
	missedLetters = ''
	correctLetters = ''
	word, wordset = hangmanGenerateWord(words)
	gameRunning = True

	while gameRunning:
		os.system('cls')
		print("\r\nHangman")
		print(f"\r\nThe word is in the set {wordset}")
		hangmanGraphics(missedLetters, correctLetters, word)
		guess = hangmanGuess(missedLetters + correctLetters)

		if guess in word:
			correctLetters += guess
			foundAllLetters = True
			for i in range(len(word)):
				if word[i] not in correctLetters:
					foundAllLetters = False
					break
			if foundAllLetters:
				os.system('cls')
				print("\r\nHangman")
				hangmanWin(gameRunning, word)
		elif guess not in word:
			missedLetters = missedLetters + guess
			if len(missedLetters) == len(HANGMAN_PICS) - 1:
				os.system('cls')
				print("\r\nHangman")
				hangmanGraphics(missedLetters, correctLetters, word)
				hangmanLose(gameRunning, word)

hangmanGame()