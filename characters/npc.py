import random
from random import randint
#can copy much from character creator

traits = []
rtittlesF = []
rtittlesM = []
ntittleF = []
ntittleM = []


#First, determine their status.
with open('info/status.txt', 'r') as file:
    statuses = file.read().splitlines()
gender = random.choice([0,1])
with open('../names/wordlists/names.txt', 'r') as file:
    names = file.read().splitlines()
with open('../names/wordlists/surnames.txt', 'r') as file:
    surnames = file.read().splitlines()
with open('jobsTitles/royalTTL.txt', 'r') as file:
    for line in file:
        f, m = line.strip().split('|')
        rtittlesF.append(f)
        rtittlesM.append(m)
with open('jobsTitles/noblestature.txt', 'r') as file:
    for line in file:
        f, m = line.strip().split('|')
        ntittleF.append(f)
        ntittleM.append(m)
with open('info/race.txt', 'r') as file:
    races = file.read().splitlines()
with open('jobsTitles/ranks.txt', 'r') as file:
    ranks = file.read().splitlines()
with open('jobsTitles/comJobs.txt', 'r') as file:
    com = file.read().splitlines()
with open('jobsTitles/begjob.txt', 'r') as file:
    beg = file.read().splitlines()
with open('background/traitsP.txt', 'r') as file:
    traitsP = file.read().splitlines()
with open('background/traitsN.txt', 'r') as file:
    traitsB = file.read().splitlines()
name = random.choice(names)
sur = random.choice(surnames)
race = random.choice(races)
test=[]
riches = 0
job = ""
print('Meet,',name,sur,' of the race ',race)
for _ in range(1):
    status = random.choice(statuses)
    if status == 'Begger':
        job = random.choice(beg)
        riches = randint(0,30)
    if status == 'Commoner':
        job = random.choice(com)
        riches = randint(30,190)
    if status == 'Knight':
        job = random.choice(ranks)
        riches = randint(80,130)
    if status == 'Noble':
        if gender == 0:
            job = random.choice(ntittleF)
        else:
            job = random.choice(ntittleM)
        riches = randint(80,600)
    if status == 'Royal':
        if gender == 0:
            job = random.choice(rtittlesF)
        else:
            job = random.choice(rtittlesM)
        riches = randint(500,1000)
    print('They are a ', status)
    print('For a living, they occupy themselves as a:', job, 'and have a whopping', riches,'on the richness index. 0 is critically poor, 1000 is obscenely rich.')

#traits
for _ in range(4):
    trait = random.choice(traitsP)
    while trait in traits:
        trait = random.choice(traitsP)
    traits.append(trait)
for _ in range(2):
    neg = random.choice(traitsB)
    while neg in traits:
        neg = random.choice(traitsB)
    traits.append(neg)
print('They are:', traits)

#Jobs, if common, occupations.txt, if noble, noblestatus, if royal

#Check if files get the right data out, and percentage for com-royal

'''commo = 0
kn = 0
nb = 0
mc = 0
for _ in range(10):
    _ = random.choice (status)
    print(_)
    if _ == "Commoner":
        commo +=1
    elif _ == 'knight':
        kn += 1
    elif _ =='Noble':
        nb += 1
    elif _ == 'Royal':
        mc += 1
print(commo,' commoners, ',kn,' knights',nb,' nobles and ', mc,'royals showed up.')'''
'''
#Check
print(rtittlesF,rtittlesM)
print(ntittleF,ntittleM)
print(com)
print(status)
print(race)
print(ranks)
print(comjob)'''