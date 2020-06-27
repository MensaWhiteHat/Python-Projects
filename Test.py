import os


def writeData():
    data = '\nI love Python!'
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()



def openFile():
    with open('test.txt', 'r') as f:
        #While the file is open, we give it the permission of read
        # and save the open file as 'f'
        data = f.read()
        #while file is open we are going to read it and store it in data
        print(data)
        #no memory leaks
        f.close()
        #you have successfully accessed an external file


if __name__=="__main__":
    writeData()
    openFile()
    #this is accessing, writing to the file and then printing it out to the screen.
