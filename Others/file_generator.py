
# just me messing around and almost killing my disk space

import os

for a in range(1, 101):
	for b in range(1, 101):
		for c in range(1, 101):
			for d in range(1, 101):
				dirName = f'cell{a}/cell{b}/cell{c}/cell{d}'
				try:
					os.makedirs(dirName)
					for i in range(1, 101):
						try:
							f = open(f"{dirName}/cell{i}.txt", "a")
							f.write("pingspoof")
						except Exception as e:
							pass
				except FileExistsError:
					pass
				print(f"sub-sub-sub-sub folder{d} deletus")
			print(f"sub-sub-sub folder{c} deletus")
		print(f"sub-sub folder{b} deletus")
	print(f"sub folder{a} deletus")
