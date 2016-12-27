<<<<<<< HEAD
#! Python3 
# savedata.py
=======
#Savedata.py
>>>>>>> d3fae44c8bf056a7e9d2dc4c8ef65405c6eb2b12

import pickle
from Player import Player

items = ["axe", "sword", "gun"]

myObj = Player(1,"JEFF", 100.00, items)
print(myObj)

with open("save2.pkl", 'wb') as outfile:
<<<<<<< HEAD
    pickle.dump(myObj, outfile,pickle.HIGHEST_PROTOCOL)
=======
	pickle.dump(myObj, outfile,pickle.HIGHEST_PROTOCOL)
>>>>>>> d3fae44c8bf056a7e9d2dc4c8ef65405c6eb2b12

print("-------------------")
newObj = None

with open("save2.pkl", 'rb') as infile:
<<<<<<< HEAD
    newObj = pickle.load(infile)

print("Printing stored data from save2.pkl")
print(newObj)
=======
	newObj = pickle.load(infile)

print(newObj)


>>>>>>> d3fae44c8bf056a7e9d2dc4c8ef65405c6eb2b12
