from tkinter import *
import tkinter

#define variables
rolls = []
max = 21
numOfRolls = int
num = int
count = int
sumOfRolls = int
average = 10

#create tkinter window
root = Tk()
root.title("DieFairnessChecker")
root.mainloop()

def isItFair(x):
    #check if the die is near the range of fair
    if x < max/2+0.6 and x > max/2-0.6:
        return("Fair")
    else:
        return("Unfair")
    
def roll(numOfRolls, max):
    cycles = int(0)
    while int(cycles) < int(numOfRolls):
        num = int(input('-'))

        if isinstance(num, int) and int(num) < max and int(num) > 0:
            rolls.append(num)
            cycles += 1
        else:
            return("Not a valid number")

def maths():
    #print out the list of rolls, an ordered list of rolls, and the average,
    print("") 
    print(rolls)
    rolls.sort()
    print(rolls)
    count = len(rolls)
    sumOfRolls = sum(list(rolls))
    average = sumOfRolls/count
    print("")
    print(average)
    print("")

print("")
print("")
print("")
print("")
print("")
print("")

print(roll(input("How many rolls? "), (int(input("How many sides on the die? "))+1)))
maths()
print(isItFair(average))