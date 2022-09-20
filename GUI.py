from tkinter import ttk
from tkinter import *
import tkinter
from tkinter import messagebox
import dice

listOfRolls = []

#functions
def getInput():
    global Input1
    string1 = Input1.get()
    Input1.pack_forget()
    label1.pack_forget()
    label3.config(text=f"Rolls: {string1}")
    
    global Input2
    string2 = Input2.get()
    Input2.pack_forget()
    label2.pack_forget()
    label4.config(text=f"Sides: {string2}")
    
    diceButton.pack_forget()

#add a roll to the list and update the average and if it's fair
def addRoll():
    global listOfRolls
    global Input3
    
    if int(Input3.get()) < int(int(Input1.get()) + 1):
        int1 = Input3.get()
        listOfRolls.append(int(int1))
        label6.config(text=f"Rolls:{listOfRolls}")
    
        string2 = dice.maths(listOfRolls)
        label7.config(text=f"Average:{string2}")
    
        label8.config(text=f"It is {dice.isItFair(string2, Input2.get())}")
    else:
        print("Dummy, that's not a roll")
        messagebox.showerror(title="STUPID", message="That's not a valid number")

#create tkinter window
root = Tk()
root.geometry("300x360")
root.title("Die Fairness Checker")

#info on the rolls
label1 = tkinter.Label(root, text = "Number of Rolls").pack()
Input1 = ttk.Entry(root).pack()

#info on the die
label2 = tkinter.Label(root, text = "How many Sides").pack()
Input2 = ttk.Entry(root).pack()

#sumbit button
diceButton = ttk.Button(root, text="Submit", width=20, command=getInput).pack(pady=30)

#confirmation labels (has the # of rolls and the # of sides in a label)
label3 = tkinter.Label(root).pack()
label4 = tkinter.Label(root).pack()

#roll input
label5 = tkinter.Label(root, text="Roll:").pack()
Input3 = ttk.Entry(root).pack()
ttk.Button(root, text="Sumbit Rolls", width=20, command=addRoll).pack(pady=10)

label6 = tkinter.Label(root, text=f"Rolls:{listOfRolls}").pack()

label7 = tkinter.Label(root, text=f"Average will show up here").pack()

label8 = tkinter.Label(root).pack()

#run the window
root.mainloop()