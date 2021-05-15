
# Phonetics Cipher made by Nicholas Johansan
# Just a made up cipher where by letters are represented by phonetics
# Every letter will be replaced by its respective phonetic
# E.g. Hello -> Hotel Echo Lima Lima Oscar

import json
import re

phonetics_dict = json.load(open("../JSON/phonetics_dict.json", 'r'))

def phonetic_of(alphabet):
	alphabet = alphabet.upper()
	for phonetic_data in phonetics_dict:
		if phonetic_data[0] == alphabet:
			return phonetic_data[1]
			break

def compile_code(text):
	compiled_text = ""
	for character in text:
		if not character.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			if character == " ":
				compiled_text += "\n"
			else:
				compiled_text += character
		else:
			compiled_text += f"{phonetic_of(character)} "
	print(compiled_text)

def decompile_code(text, r=False):
	decompiled_text = ""
	for phonetic in text.split():
		decompiled_text += f"{phonetic[0].lower()}"
	if r == True:
		return decompiled_text
	else:
		print(decompiled_text)

def decompile_multiple(text):
	decompiled_text = ""
	for word in text.splitlines():
		decompiled_text += f"{decompile_code(word, True)} "
	print(decompiled_text)

# Usage for single word
#compile_code("hello")
#decompile_code("Hotel Echo Lima Lima Oscar")

# When there is multiple words, a decompile_multiple is needed
#compile_code("a message with multiple words")
#decompile_multiple("""Alfa 
#Mike Echo Sierra Sierra Alfa Golf Echo 
#Whiskey India Tango Hotel 
#Mike Uniform Lima Tango India Papa Lima Echo 
#Whiskey Oscar Romeo Delta Sierra""")
