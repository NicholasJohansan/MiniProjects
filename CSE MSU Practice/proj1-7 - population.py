#https://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Population/project01.pdf
import os
CURRENT_POPULATION = 307_357_870
while True:
	yrs = input(f"\r\nCurrent population size: {CURRENT_POPULATION:,}\nInput number of years into the future\n>> ")
	try:
		yrs = int(yrs)
	except ValueError:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		seconds = yrs * 365 * 24 * 60 * 60
		deaths = seconds // 13
		births = seconds // 7
		immigrants = seconds // 35
		os.system('cls')
		net_change = immigrants + births - deaths
		new_population = CURRENT_POPULATION + net_change
		input(f"\r\nCurrent Population: {CURRENT_POPULATION:,}\nNew Population: {new_population:,}\nNet Change: {'-' if net_change < 0 else '+'}{net_change:,}\nPress [Enter] to enter another value:")
		os.system('cls')