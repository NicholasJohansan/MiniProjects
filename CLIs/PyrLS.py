
# PyrLS written by Nicholas Johansan
# a Link Shortcuts CLI
# You can store links and access it by entering its corresponding number
# This was part of me learning how to store data in AppData folder

import webbrowser, sys, os, json
from validators import url

def create_defaults(path, version, user=False):
	dynamicenv = {
			"version": version,
			"websites": []
	}
	if user:
		dynamicenv['websites'] = json.load(open(path, 'r'))['websites']
	json.dump(dynamicenv, open(path, 'w'))

version = 0.1
dir_path = os.path.join(os.environ['APPDATA'], 'dynamicenv') #path AppData/Roaming/dynamicenv
if not os.path.exists(dir_path):
	os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'dynamic.json') #path AppData/Roaming/dynamicenv/dynamic.json
if not os.path.exists(file_path):
	create_defaults(file_path, version)
elif json.load(open(file_path, 'r'))['version'] != version:
	create_defaults(file_path, version, True)

'''
Example data struct of website for reference
"websites":[
{
	"url": "https://google.com",
	"name": "Google"	
},
{
	"url": "https://tinyurl.com",
	"name": "TinyURL"
}
]
'''

while True:
	dynamicdata = json.load(open(file_path, 'r'))
	options = ["exit"]
	res = None
	if len(dynamicdata['websites']) == 0:
		res = input(f"Welcome to PyrLS v{version}!\nYou have no shortcuts stored!\nYou can create a shortcut to a website by typing \"create\"\nor you can exit the program by typing \"exit\"\n>> ").lower()
		options.append("create")
	else:
		msg = f"Welcome to PyrLS v{version}!\nEnter the respective number of the website you want to go to!\n"
		for web in dynamicdata['websites']:
			msg += f"- [{dynamicdata['websites'].index(web)+1}] {web['name']}\n"
		msg += "You can create another shortcut by typing \"create\" or remove a shortcut by typing \"remove\"\nTo exit, you can type \"exit\"\n>> "
		res = input(msg).lower()
		options = ["exit", "create", "remove"]
	os.system('cls')
	if res in options:
		if res == "exit":
			sys.exit()
		elif res == "create":
			web = {
				"url": "",
				"name": ""
			}
			while True:
				urli = input("\rEnter a valid website URL you want to make a shortcut for.\nFor instance, \"https://google.com\", \"http://tinyurl.com\". Remember to include \"http://\" in front!\n>> ")
				if url(urli):
					web['url'] = urli
					break
				else:
					os.system('cls')
					print("Invalid URL provided!\n")
					continue
			os.system('cls')
			web['name'] = input("\rWhat do you want the shortcut to be called?\nIt will just be used as a label to help you identify the shortcut.\n>> ")
			dynamicdata['websites'].append(web)
			json.dump(dynamicdata, open(file_path, 'w'))
			os.system('cls')
			print(f"\rShortcut [{web['name']}] with URL [{web['url']}] have been created!\n")
		elif res == "remove":
			while True:
				msg = "\rWhich shortcut do you want to remove?\nEnter the respective number corresponding to the shortcut.\n"
				for web in dynamicdata['websites']:
					msg += f"- [{dynamicdata['websites'].index(web)+1}] {web['name']}: {web['url']}\n"
				msg += "or you can type \"cancel\" to cancel.\n>> "
				res = input(msg).lower()
				if res == "cancel":
					os.system('cls')
					break
				else:
					try:
						int(res)
					except ValueError:
						os.system('cls')
						print("\rYou did not enter any of the options! Try again!\n")
					else:
						res = int(res)
						if res in range(1, len(dynamicdata['websites'])+1):
							dynamicdata['websites'].pop(res-1)
							json.dump(dynamicdata, open(file_path, 'w'))
							os.system('cls')
							print("\rShortcut have been removed!\n")
							break
						else:
							os.system('cls')
							print("\rThe number you entered wasn't on the list of shortcuts! Try again!\n")
							continue
	else:
		try:
			int(res)
		except ValueError:
			os.system('cls')
			print(f"\rYou did not enter any of the options!\n{res} isn\'t an available option! Try again!\n")
		else:
			res = int(res)
			if res in range(1, len(dynamicdata['websites'])+1):
				web = dynamicdata['websites'][res-1]
				webbrowser.open(web['url'])
				os.system('cls')
				print(f"\rShortcut [{web['name']}] with URL [{web['url']}] have been opened!\n")
			else:
				os.system('cls')
				print("\rThe number you entered wasn't on the list of shortcuts! Try again!\n")
				continue
