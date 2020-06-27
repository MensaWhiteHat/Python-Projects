#create a script
import os

dirloc = "C:\\A\\"

for file in os.listdir(dirloc):
    if file.endswith(".txt"):
        print(os.path.join(dirloc, file))
    else:
        continue

for file in os.listdir(dirloc):
    if file.endswith(".txt"):
        print(os.path.getmtime(file))
    else:
        continue
