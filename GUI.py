from cProfile import label
from tkinter import *
import tkinter
import dice

#create tkinter window
root = Tk()
root.title("DieFairnessChecker")

#widgets
Label1 = tkinter.Label(root, text="Test")
Label1.pack()

label2 = tkinter.Label(root, text=f"||{dice.testfunc}||")
label2.pack()

#run the window
root.mainloop()