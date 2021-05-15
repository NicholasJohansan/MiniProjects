#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Richter/project01.pdfimport os
import os
while True:
	magnitude = input("\r\nInput Richter Scale\n>> ")
	try:
		magnitude = float(magnitude)
	except Exception as E:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		os.system('cls')
		energy = 10**((1.5*magnitude)+4.8)
		tons_of_tnt = energy/(4.184*(10**9))
		input(f"\r\nRichter Scale Value: {magnitude}\nJoules: {energy}J\nTons of TNT: {tons_of_tnt}\n\nPress [Enter] to input more values:")
		os.system('cls')