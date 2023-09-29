import random
from random import randint

halfbreed_races = ['dwarf', 'elf', 'human', 'gnome', 'pelode', 'fairy', 'mermaid', 'orc', 'unknown']
stats = ["str","dex","con","intg","wis","char"]
other_parent = ""
allignment_vertical = ['lawful','neutral','chaotic']
allignment_horizontal = ['good','neutral','evil']
combo = ""
bg = []
calling = []
tradg = []
traits = []
happy = []
throw = []
total = []
halfbreed = False
summed = 0

#Dice throw
for j in range(6):
    for i in range(4):
        new_throw = randint(1, 6)
        throw.append(new_throw)
        new_stat = f"stat{i}"
    #print("Fikk:", throw)
    throw.sort(reverse=True)
    discard = throw.pop()
    total.append(sum(throw))
    #print("Fjerner laveste kast, får da:")
    #print(throw,"sum:",sum((throw)))
    throw = []

#Alignment
allignV = random.choice(allignment_vertical)
combo += allignV
allignH = random.choice(allignment_horizontal)
combo += " "
combo += allignH
if allignH == allignV:
    combo = "true Neutral"

with open('info/race.txt', 'r') as file:
    races = file.read().splitlines()
#Race
random_race = random.choice(races)
if random_race in halfbreed_races:
    half = randint(1,100)
    if half < 40:
        halfbreed = True
    if halfbreed:
        other_parent = random.choice(halfbreed_races)

with open('info/classes.txt', 'r') as file:
    classes = file.read().splitlines()
#calling
for _ in range(2):
    rand_call = random.choice(classes)
    while rand_call in calling:
        rand_call = random.choice(classes)
    calling.append(rand_call)

with open('background/background.txt', 'r') as file:
    background = file.read().splitlines()
#Background
for _ in range(2):
    rand_bg = random.choice(background)
    while rand_bg in bg:
        rand_bg = random.choice(background)
    bg.append(rand_bg)

with open('background/happy.txt', 'r') as file:
    happiness = file.read().splitlines()
#happiness in bg
for _ in range(3):
    good = random.choice(happiness)
    while good in happy:
        good = random.choice(happiness)
    happy.append(good)

with open('background/tradgedy.txt', 'r') as file:
    tradgedies = file.read().splitlines()
#tradgedies
for _ in range(3):
    tradgedy = random.choice(tradgedies)
    while tradgedy in tradg:
        tradgedy = random.choice(tradgedies)
    tradg.append(tradgedy)

with open('background/traitsP.txt', 'r') as file:
    traitsP = file.read().splitlines()
with open('background/traitsN.txt', 'r') as file:
    traitsB = file.read().splitlines()
#traits
for _ in range(4):
    trait = random.choice(traitsP)
    while trait in traits:
        trait = random.choice(traitsP)
    traits.append(trait)
for _ in range(2):
    traitN = random.choice(traitsB)
    while traitN in traits:
        traitN = random.choice(traitsB)
    traits.append(traitN)

if halfbreed:
    print("Congratulations! You're a halfbreed! Your parents are:", random_race, "and", other_parent)
else:
    print("Congratulations! You're a ",random_race)
print("You can choose from one of these two backgrounds, should you wish.",bg)
print("You can choose between these two classes:", calling, "That's what your 'calling' is. How you do things.")
print("You can choose between these traits: take as many or few as you'd like!",traits)
print("In your past this event/experience shaped you in a significant way:", happy)
print("Should you want a tradgedy in your past, take one of these:", tradg)
print("Your allignment is:", combo)
print("Your toatal scores were:", total)
print("They can either be assigned according to this list:")
for item, tot in zip(stats, total):
    if tot < 2:
        print(item, tot, "With Ability modifier: -5")
    else:
        ability_modifier = (tot - 10) // 2
        print(item, tot, f"Ability modifier: {ability_modifier}.")

print("Or, you can choose them yourself, keep your class in mind when you choose what stats to assign what skills. ")
print("Remember that based on your race, background and class, you may have extra skillpoints in certain categories.")
