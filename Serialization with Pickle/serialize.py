#! Python3
# serialize.py

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

pickle.dump(dict1, output,pickle.HIGHEST_PROTOCOL) # Saving the Dictionary in the pickle file
pickle.dump(list1, output,pickle.HIGHEST_PROTOCOL) # Saving the List in the pickle file

output.close()

print("------------------")

inputFile = open("save1.pkl", 'rb')                # Opening the pickle file

dict2 = pickle.load(inputFile)                     # Loading the Dictionary from the pickle file 
list2 = pickle.load(inputFile)                     # Loading the List from the pickle file   

inputFile.close()

# Printing the restored results from the pickle file
print("Printing stored data from " + str(inputFile.name))
print(dict2)
print(list2)

