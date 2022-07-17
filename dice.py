#define variables
cycles = int(0)
rolls = []
max = 21
numOfRolls = int
num = int
count = int
sum = int
average = int

#check if the die is near the range of fair
def isItFair(x):
    if x < 11 and x > 9:
        return("Fair")
    else:
        return("Unfair")

#print out the list of rolls, an ordered list of rolls, and the average, 
def maths():
    print(rolls)
    rolls.sort()
    print(rolls)
    count = len(rolls)
    sum = sum(rolls)
    average = sum/count
    print(average)

print("Input a roll by typing a number and pressing enter")
numOfRolls = input("How many rolls? ")

#take numOfRolls inputs
while int(cycles) < int(numOfRolls):
    num = int(input('-'))

    if isinstance(num, int) and int(num) < max and int(num) > 0:
        rolls.append(num)
        cycles += 1
    else:
        print("Not a valid number")

maths()

print(isItFair(average))