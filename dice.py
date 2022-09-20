#define variables
rolls = []
numOfRolls = int
num = int
count = int
sumOfRolls = int
average = 10

def isItFair(x, max):
    #check if the die is near the range of fair
    if x < int(max)/2+0.6 and x > int(max)/2-0.6:
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

def maths(x):
    count = len(x)
    sumOfRolls = sum(list(x))
    average = sumOfRolls/count
    return(average)

#max = input("How many sides on the die? ")
#print(roll(input("How many rolls? "), (int(max))))
#print(isItFair(maths(rolls), max))