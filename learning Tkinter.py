#Do make Recall notes of this as well

import tkinter
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master): #, *args, **kwargs
        Frame.__init__(self) #first three lines should be used always. understand its doing later

        self.master = master #have to use when referencing class items
        self.master.resizable(width = True, height = True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='darkgray')

        self.varFName = StringVar() #instantiated and then passed to varfname
        self.varLName = StringVar()

        #invoke labels
        self.lblFName = Label(self.master, text='First Name', font=("Helvetica", 16), fg= 'black', bg='lightblue')
        self.lblFName.grid(row=0 , column=0, padx=(30, 0) , pady=(30, 0))
        
        self.lblLName = Label(self.master, text='Last Name', font=("Helvetica", 16), fg= 'black', bg='lightblue')
        self.lblLName.grid(row=1 , column=0, padx=(30, 0) , pady=(30, 0))

        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg= 'black', bg='lightblue')
        self.lblDispaly.grid(row=3, column=1, padx=(30, 0) , pady=(30, 0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg= 'black', bg='lightblue') #we know this is a tuple because of ""
        self.txtFName.grid(row=0, column=1, padx=(30, 0) , pady=(30, 0)) #command to paint
        
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg= 'black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30, 0) , pady=(30, 0))

        #btns
        self.btnSubmit = Button(self.master, text="Submit", command= self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(00, 0) , pady=(30, 0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", command= self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0 ,90) , pady=(30, 0), sticky=NE)


    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDispaly.config(text = 'Howdy, {} {}!'.format(fn, ln))   #to get it to function 

        
    def cancel(self):
        self.master.destroy()

        
        
if __name__ == "__main__" :
#we instantiated the class and now we have an instance of it, and named it root
    root = Tk()
    App = ParentWindow(root)
    #most important line follow
    root.mainloop()
