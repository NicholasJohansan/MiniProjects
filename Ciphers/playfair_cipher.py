
# Playfair Cipher written by Nicholas Johansan
# Inspiration/Guidance from http://homepages.math.uic.edu/~lenz/f15.m260/project1.html
# Date: 6th June 2020 5pm - 8:30pm [3 hours 30 mins]

def test_existence(char, table):
	for row in table:
		if char in row:
			return True
	return False

def gen_table(key):
	key = (key.upper()).replace("J", "I")
	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	table = [
		[],
		[],
		[],
		[],
		[]
	]

	row = 0
	for char in key.upper():
		if not test_existence(char, table) and char in alphabet:
			if len(table[row]) == 5:
				row += 1
			table[row].append(char)

	for char in alphabet:
		if not test_existence(char, table):
			if len(table[row]) == 5:
				row += 1
			table[row].append(char)

	return table

def find_char(char, table):
	for row in table:
		if char in row:
			return table.index(row), row.index(char)

def boundary_handler(point):
	#for encoding
	if point == 4:
		return 0
	return point+1

def boundary_handler2(point):
	#for decoding
	if point == 0:
		return 4
	return point-1

def encode_pair(a, b, table):
	if a == b:
		print("error")

	a_row, a_col = find_char(a, table)
	b_row, b_col = find_char(b, table)

	#print(f"{a}(row: {a_row}, column: {a_col}), {b}(row: {b_row}, column: {b_col})")
	
	if a_col == b_col:
		return(f"{table[boundary_handler(a_row)][a_col]}{table[boundary_handler(b_row)][b_col]}")
	elif a_row == b_row:
		return(f"{table[a_row][boundary_handler(a_col)]}{table[b_row][boundary_handler(b_col)]}")
	else:
		return(f"{table[a_row][b_col]}{table[b_row][a_col]}")

def decode_pair(a, b, table):
	if a == b:
		print("error")

	a_row, a_col = find_char(a, table)
	b_row, b_col = find_char(b, table)

	if a_col == b_col:
		return(f"{table[boundary_handler2(a_row)][a_col]}{table[boundary_handler2(b_row)][b_col]}")
	elif a_row == b_row:
		return(f"{table[a_row][boundary_handler2(a_col)]}{table[b_row][boundary_handler2(b_col)]}")
	else:
		return(f"{table[a_row][b_col]}{table[b_row][a_col]}")

def format(text):
	cleaned = ""
	for char in text.upper():
		if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			if char == "J":
				char = "I"
			cleaned += char
	if len(cleaned)%2 == 1 or cleaned[len(cleaned)-1] == cleaned[len(cleaned)-2]:
		cleaned += "Z"
	first = ""
	pairs = []
	for char in cleaned:
		if first == "":
			first = char
		elif first:
			if first == char:
				pairs.append(f"{first}X")
				first = char
			else:
				pairs.append(f"{first}{char}")
				first = ""
	return pairs

def decode_format(text):
	cleaned = ""
	for char in text.upper():
		if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			cleaned += char
	first = ""
	pairs = []
	for char in cleaned:
		if first == "":
			first = char
		elif first:
			pairs.append(f"{first}{char}")
			first = ""
	return pairs

def encode(text, key):
	compiled_text = ""
	table = gen_table(key)
	pairs = format(text)
	for char1, char2 in pairs:
		compiled_text += encode_pair(char1, char2, table)
	print(compiled_text)

def decode(text, key):
	decompiled_text = ""
	predecompiled_text = ""
	table = gen_table(key)
	pairs = decode_format(text)
	for char1, char2 in pairs:
		predecompiled_text += decode_pair(char1, char2, table)
	for char in predecompiled_text:
		if char != "X" and char != "Z":
			decompiled_text += char

	print(decompiled_text)

# Usage
#encode("A hidden message", "key") #BGLCLDONAQXGDA
#decode("BGLCLDONAQXGDA", "key") #AHIDDENMESSAGE
