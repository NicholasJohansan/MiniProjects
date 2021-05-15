#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/FirstWeekProjects/Arithmetic/project01.pdf
import os
while True:
	n1 = input("\r\nInput First Integer\n>> ")
	try:
		n1 = int(n1)
	except Exception as E:
		os.system('cls')
		print("\r\nYou did not give a number, try again.")
	else:
		n2 = input("\r\nInput Second Integer\n>> ")
		try:
			n2 = int(n2)
		except Exception as E:
			os.system('cls')
			print("\r\nYou did not give a number, try again.")
		else:
			os.system('cls')
			_sum = n1+n2
			diff = n1-n2
			prod = n1*n2
			quot = n1/n2
			input(f"\r\nFirst Integer: {n1}\nSecond Integer: {n2}\nSum of {n1} and {n2}: {_sum}\nDifference of {n1} and {n2}: {diff}\nProduct of {n1} and {n2}: {prod}\nQuotient of {n1} and {n2}: {quot}\n\nPress [Enter] to input more values:")
			os.system('cls')