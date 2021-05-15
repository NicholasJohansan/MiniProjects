#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Canoe_Portage/project01.pdf
import os

while True:
	rods = input("\r\nInput rods\n>> ")
	try:
		rods = float(rods)
	except Exception as E:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		os.system('cls')
		meter = rods * 5.0292
		furlong = rods/40
		mile = meter/1609.34
		foot = meter/0.3048
		time = (mile/3.1)*60
		input(f"\r\n{rods} rods:\nMeters: {meter}\nFeet: {foot}\nMiles: {mile}\nFurlongs: {furlong}\nWalking time in minutes: {time}\nPress [Enter] to input more values:")
		os.system('cls')