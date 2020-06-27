import os

fName = 'Hello.txt'

fPath = 'C:\\A\\'

#os.path.join(path, *paths)

abPath = os.path.join(fPath, fName)
print(abPath)
#this is how you create an abolute file path. 
