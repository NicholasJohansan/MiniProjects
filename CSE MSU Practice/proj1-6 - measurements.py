#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Measurement/project01.pdf
import os
while True:
	mph = input("\r\nInput miles per hour (mph)\n>> ")
	try:
		mph = float(mph)
	except Exception as E:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		os.system('cls')
		barleycorns_day = mph * (1609.34*117.647*24)
		furlongs_fortnight = mph * (24*14*8)
		mach = (mph * (5280/3600))/1130
		psl = ((mph * (1609.344/3600))/299792458) * 100
		input(f"\r\nmph: {mph}\nbarleycorn/day: {barleycorns_day}\nfurlong/fortnight: {furlongs_fortnight}\nMach: {mach}\n% of speed of light: {psl}%\n\nPress [Enter] to input more values:")
		os.system('cls')