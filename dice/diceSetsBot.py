from random import *

#Establish existing dice
diceSet = [2, 4, 6, 8, 10, 12, 20]
#Input query
diceString = input("XdY where x is amount rolled, and y is dicetype, \n can also do multiple, ex. 2d6+3d4+...+n:")

#Defining a function that takes the parameters
def roll_dice(amount, sides):
    return [randint(1,sides) for _ in range(amount)]

total_random = []
total_sum = 0
#Dividing the prompt by the plus
if '+' in diceString:
    dice_expression = diceString.split('+')

#For the ones with more appendixes
    for expression in dice_expression:
        amount, sides = expression.split('d')
        amount = int(amount)
        sides = int(sides)
        if sides in diceSet:
            dice_results = roll_dice(amount, sides)
            total_random.extend(dice_results)
            total_sum += sum(dice_results)
        else:
            print("Error: Dice doesn't exists. Try again. possible dice: 2, 4, 6, 8, 10, 12, 20")
#For the ones with only one dice rolled many times
else:
    amount, sides = diceString.split('d')
    amount = int(amount)
    sides = int(sides)
    if sides in diceSet:
        dice_results = roll_dice(amount, sides)
        total_random.extend(dice_results)
        total_sum += sum(dice_results)
    else:
        print("Error: Dice doesn't exists. Try again. possible dice: 2, 4, 6, 8, 10, 12, 20")

print(total_random)
print(total_sum)
'''
    values = diceString.split('+')  # Deler stringen opp i values der + er
    valueslen = len(values) #Assigns length of values to valueslen, as in how many values are in it
    amount_sett = []
    dice_sett = [] 

    for value in values:
        amount, dice = value.split('d')
        amount_sett.append(int(amount))
        dice_sett.append(int(dice))

    random_num = []

    for amount, sides in zip(amount_sett,dice_sett):
        sides_list = diceSet[:diceSet.index(sides) + 1]
        random_num.extend([randint(1, side)for side in sides_list] * amount)
    
    
    print(values)
    print(amount_sett, dice_sett)
    print(random_num)
    '''
    #Må hente ut første og andre var fra settene for å få kaste terninger
