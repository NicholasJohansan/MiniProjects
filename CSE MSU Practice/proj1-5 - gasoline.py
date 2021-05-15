#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Gasoline/project01.pdf
import os
while True:
	gallons = input("\r\nInput Gallons of Gasoline\n>> ")
	try:
		gallons = float(gallons)
	except Exception as E:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		os.system('cls')
		liters = gallons * 3.7854
		barrels = gallons/19.5
		co2 = gallons * 20
		ethanol = gallons * (115000/75700)
		cost = gallons * 4
		input(f"\r\nGallons of gas: {gallons}\nLitres of gas: {liters}J\nBarrels of oil: {barrels}\nCO2 produced: {co2}\nGallons of ethanol: {ethanol}\nCost: ${cost}\n\nPress [Enter] to input more values:")
		os.system('cls')