
# copyrename written by Nicholas Johansan
# a CLI made for my friend who wanted a quick way to rename textures

import argparse, string

def func(clone_letter, constant_name, excluded_letters, last_letter, start_letter, lowercase):

	constant_name = f"{constant_name}.png"
	data = open(constant_name.replace("/", clone_letter), "rb").read()

	excluded_letters = clone_letter + excluded_letters

	letters = string.ascii_uppercase
	if lowercase:
		letters = string.ascii_lowercase

	a, b, c = letters.partition(start_letter)

	letters = b+c

	a, b, c = letters.partition(last_letter)

	letters = a+b

	for letter in excluded_letters:
		letters = letters.replace(letter, "")

	for letter in letters:
		open(constant_name.replace("/", letter), "wb").write(data)

parser = argparse.ArgumentParser(description='A utility for Pixo')
parser.add_argument('-e', help="excluded letters in ABC format; Default: none", default="", type=str)
parser.add_argument("-c", help="1 capital letter; a letter for cloning. Default: A", default="A", type=str)
parser.add_argument("-s", help="1 capital letter; indicates start letter. Default: A", default="A", type=str)
parser.add_argument("-l", help="1 capital letter; indicates last letter. Default: Z", default="Z", type=str)
parser.add_argument("-d", help="structure of filename; / to indicate letter placement. For example: QCGC/0", type=str)
parser.add_argument("-lower", help="include -lower to switch to lowercase", action="store_true")

args = parser.parse_args()
func(args.c, args.d, args.e, args.l, args.s, args.lower)