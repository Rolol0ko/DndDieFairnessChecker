from tkinter import ttk
from tkinter import *
import tkinter
import dice

listOfRolls = []

#functions
def getInput():
    global Input1
    string1 = Input1.get()
    label3.config(text=f"Rolls: {string1}")
    
    global Input2
    string2 = Input2.get()
    label4.config(text=f"Sides: {string2}")
    
def addRoll():
    global listOfRolls
    global Input3
    string1 = Input3.get()
    listOfRolls.append(string1)
    label6.config(text=f"Rolls:{listOfRolls}")
    label7.config(text=f"Average:{dice.maths(listOfRolls)}")

#create tkinter window
root = Tk()
root.geometry("300x360")
root.title("Die Fairness Checker")

#info on the die
label1 = tkinter.Label(root, text = f"Number of Rolls")
label1.pack()
Input1 = ttk.Entry(root)
Input1.pack()

#info on the rolls
label2 = tkinter.Label(root, text = f"How many Sides")
label2.pack()
Input2 = ttk.Entry(root)
Input2.pack()

#sumbit button
ttk.Button(root, text="Submit", width=20, command=getInput).pack(pady=30)

#confirmation labels (has the # of rolls and the # of sides in a label)
label3 = tkinter.Label(root)
label3.pack()
label4 = tkinter.Label(root)
label4.pack()

label5 = tkinter.Label(root, text="Roll:")
label5.pack()
Input3 = ttk.Entry(root)
Input3.pack()
ttk.Button(root, text="Sumbit Rolls", width=20, command=addRoll).pack(pady=10)

label6 = tkinter.Label(root, text=f"Rolls:{listOfRolls}")
label6.pack()

label7 = tkinter.Label(root, text=f"___")
label7.pack()

#run the window
root.mainloop()