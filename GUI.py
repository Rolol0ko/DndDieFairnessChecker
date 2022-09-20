from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import tkinter
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
    
    #check if it's a valid roll
    if int(Input3.get()) < int(int(Input1.get()) + 1):
        int1 = Input3.get()
        listOfRolls.append(int(int1))
        label6.config(text=f"Rolls:{listOfRolls}")
    
        string2 = dice.maths(listOfRolls)
        label7.config(text=f"Average:{string2}")
    
        label8.config(text=f"It is {dice.isItFair(string2, Input2.get())}")
    else:
        messagebox.showerror(title="STUPID", message="That's not a valid number")

#create tkinter window
root = Tk()
root.geometry("300x360")
root.title("Die Fairness Checker")

#info on the rolls
label1 = tkinter.Label(root, text = "Number of Rolls")
label1.pack()
Input1 = ttk.Entry(root)
Input1.pack()

#info on the die
label2 = tkinter.Label(root, text = "How many Sides")
label2.pack()
Input2 = ttk.Entry(root)
Input2.pack()

#sumbit button
diceButton = ttk.Button(root, text="Submit", width=20, command=getInput)
diceButton.pack(pady=30)

#confirmation labels (has the # of rolls and the # of sides in a label)
label3 = tkinter.Label(root)
label3.pack()
label4 = tkinter.Label(root)
label4.pack()

#roll input
label5 = tkinter.Label(root, text="Roll:")
label5.pack()
Input3 = ttk.Entry(root)
Input3.pack()
ttk.Button(root, text="Sumbit Rolls", width=20, command=addRoll).pack(pady=10)

label6 = tkinter.Label(root, text=f"Rolls:{listOfRolls}")
label6.pack()

label7 = tkinter.Label(root, text=f"Average will show up here")
label7.pack()

label8 = tkinter.Label(root)
label8.pack()

#run the window
root.mainloop()