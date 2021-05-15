#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/WindChill/project01.pdf
import os
while True:
	temp = input("\r\nInput Air Temperature in °F\n>> ")
	try:
		temp = float(temp)
	except Exception as E:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		windspeed = input("\r\nInput Wind Speed in mph\n>> ")
		try:
			windspeed = float(windspeed)
		except Exception as E:
			os.system('cls')
			print("\r\nYou did not give a number, try again.")
		else:
			os.system('cls')
			wct = 35.74+(0.6215*temp)-(35.75*(windspeed**0.16))+((0.4275*temp)*(windspeed**0.16))
			input(f"\r\nTemperature: {temp}°F\nWindspeed: {windspeed}mph\nWind Chill Temperature Index: {wct}°F\n\nPress [Enter] to input more values:")
			os.system('cls')