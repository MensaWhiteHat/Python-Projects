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
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tinkter Phonebook Demo")
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
