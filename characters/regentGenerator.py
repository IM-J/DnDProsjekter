import random

data = {}
underGov  = ['bureaucracy', 'democracy']
power = ['feudalism','militocracy']
absolute = ['autocracy','dictatorship','hierarchy','monarchy']
with open('government.txt','r') as file:
    for line in file:
        govern, desc = line.strip().split('|')
        data[govern] = desc
gender = random.choice([0,1])
with open('../names/wordlists/names.txt', 'r') as file:
    names = file.read().splitlines()
with open('../names/wordlists/surnames.txt', 'r') as file:
    surnames = file.read().splitlines()
with open('../names/wordlists/namesSaved.txt', 'r') as file:
    kns = file.read().splitlines()
with open('info/race.txt', 'r') as file:
    races = file.read().splitlines()
with open('background/traitsP.txt', 'r') as file:
    traitsP = file.read().splitlines()
with open('background/traitsN.txt', 'r') as file:
    traitsB = file.read().splitlines()
traits = ""
#traits
for _ in range(4):
    trait = random.choice(traitsP)
    while trait in traits:
        trait = random.choice(traitsP)
    traits += trait
    traits += " "
for _ in range(2):
    traitN = random.choice(traitsB)
    while traitN in traits:
        traitN = random.choice(traitsB)
    traits += traitN
    traits += " "
kingdom = random.choice(kns)
name = random.choice(names)
sur = random.choice(surnames)
type = random.choice(list(data.keys()))
race = random.choice(races)

print("Welcome to ", kingdom,". Meet",name,sur,"they are the one in charge around here. Know that they are known to be ",traits," This area is considered to be similair to ")
print(f"{type}, which means: \n {data[type]}")

