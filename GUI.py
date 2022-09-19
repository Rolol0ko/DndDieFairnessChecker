from tkinter import ttk
from tkinter import *
import tkinter
import dice

#create tkinter window
root = Tk()
root.geometry("300x300")
root.title("DieFairnessChecker")

#widgets
label2 = tkinter.Label(root, text=f"{dice.isItFair(5,2.5)}")
label2.pack()

Input = ttk.Entry(root)
Input.pack()

#run the window
root.mainloop()