
#define variables
cycles = int(0)
rolls = []
max = 21
numOfRolls = int
num = int
count = int
sumOfRolls = int
average = 10

def isItFair(x):
    #check if the die is near the range of fair
    if x < max/2+0.6 and x > max/2-0.6:
        return("Fair")
    else:
        return("Unfair")
    
def rolls():
    #take numOfRolls inputs
    while int(cycles) < int(numOfRolls):
        num = int(input('-'))

        if isinstance(num, int) and int(num) < max and int(num) > 0:
            rolls.append(num)
            cycles += 1
        else:
            print("Not a valid number")

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

print("Input a roll by typing a number and pressing enter")
numOfRolls = input("How many rolls? ")
max = (int(input("How many sides on the die?"))+1)

rolls()
maths()
print(isItFair(average))