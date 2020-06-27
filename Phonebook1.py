# Author: Samuel Spinda
#
# Note: Create your GUI prior to coding
#
# Purpose: To create a phonebook 
#

from tkinter import *
import tkinter as tk

#be sure to import other modules to have access
import phonebook_gui
import phonebook_func

#frame is the tkinter frame class that we will inhert from
class ParentWindow(Frame): #primary tkinter object
    def __init__(self, master, *args, **kwargs): #define class with self
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master #master level frame
        self.master.minsize(500, 300) #height , width
        self.master.maxsize(500, 300) # self is always refering to parent window
        phonebook_func.center_window(self,500,300) #reference to outer script, already imported at top. always center in user screen.
        #you have to pass in self as a key.
        self.master.title("The Tinkter Phonebook Demo") #the eveything frame will be titled...
        self.master.configure(bg = "maroon")
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self)) #rule for master designated by windows
        arg = self.master

        phonebook_gui.load_gui(self) #loading expansive widgets


if __name__ == "__main__": #"if we run this script, then the tkinter syntax, the app class root and its loop are required."
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
