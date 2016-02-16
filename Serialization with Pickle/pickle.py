//pickling.py//

import pickle

dict1 = {'a': 100,
	'b': 200,
	'c': 300}

list1 = [400,
	500,
	600]

print(dict1)
print(list1)

output = open("save1.pkl", 'wb')

pickle.dump(dict1, output,pickle.HIGHEST_PROTOCOL)
pickle.dump(list1, output,pickle.HIGHEST_PROTOCOL)

output.close()

print("------------------")

inputFile = open("save1.pkl", 'rb')

dict2 = pickle.load(inputFile)
list2 = pickle.load(inputFile)

inputFile.close()

print(dict2)
print(list2)

//Player.py//

class Player:

	def __init__(self, ID, name, health, items):
		self.id = ID
		self.name = name
		self.health = health
		self.items = items

	def __str__(self):
		return "My ID: " + str(self.id) + \
			" \nMy Name: " + self.name + \
			" \nMy Health: " + str(self.health) + \
			" \nMy Items: " + str(self.items) + "."

//savedata.py//

import pickle
from Player import Player

items = ["axe", "sword", "gun"]

myObj = Player(1,"JEFF", 100.00, items)
print(myObj)

with open("save2.pkl", 'wb') as outfile:
	pickle.dump(myObj, outfile,pickle.HIGHEST_PROTOCOL)

print("-------------------")
newObj = None

with open("save2.pkl", 'rb') as infile:
	newObj = pickle.load(infile)

print(newObj)


