import random
from random import randint
import string
#puts together words anad or letters into names. The letters are added according to percentage of times it shows up in english language.
vow = "aaaaaaaaeeeeeeeeeeeeeiiiiiiioooooooouuuyyæøå"
cons = "bbcuuddddffgghhhhhjklllllmmmnnnnnnnppqrrrrrrrsssssstttttttttvwwxz"
special = "' -"
names = []
alt = ""
consec_cons = 0
consec_vow = 0
with open('wordlists/adjectives.txt', 'r') as file:
    adj = file.read().splitlines()
with open('wordlists/nouns.txt', 'r') as file:
    nouns = file.read().splitlines()
with open('wordlists/verbs.txt', 'r') as file:
    vb = file.read().splitlines()

#noun, vb
for _ in range(randint(5,10)):
    ran_noun = random.choice(nouns)
    alt += ran_noun
    alt +=" "
    randVB = random.choice(vb)
    alt += randVB
    names.append(alt)
    alt = ""
#VB, noun
for _ in range(randint(5,10)):
    randVB = random.choice(vb)
    alt += randVB
    alt +=" "
    ran_noun = random.choice(nouns)
    alt += ran_noun
    names.append(alt)
    alt = ""
#vb, adj
for _ in range(randint(5,10)):
    randAdj = random.choice(adj)
    alt += randAdj
    alt +=" "
    ran_noun = random.choice(nouns)
    alt += ran_noun
    names.append(alt)
    alt = ""
#adj, vb
for _ in range(randint(5,10)):
    randAdj = random.choice(adj)
    alt += randAdj
    alt +=" "
    randVB = random.choice(vb)
    alt += randVB
    names.append(alt)
    alt = ""

#noun, adj
for _ in range(randint(5,10)):
    ran_noun = random.choice(nouns)
    alt += ran_noun
    alt +=" "
    randAdj = random.choice(adj)
    alt += randAdj
    names.append(alt)
    alt = ""

#Adj,noun
for _ in range(randint(5,10)):
    randAdj = random.choice(adj)
    alt += randAdj
    alt +=" "
    ran_noun = random.choice(nouns)
    alt += ran_noun
    names.append(alt)
    alt = ""

#noun on Noun
for _ in range(randint(5,10)):
    ran_noun = random.choice(nouns)
    alt += ran_noun
    alt +=" "
    ran_noun = random.choice(nouns)
    alt += ran_noun
    names.append(alt)
    alt = ""

#noun on noun on Noun
for _ in range(randint(5,10)):
    ran_noun = random.choice(nouns)
    alt += ran_noun
    ran_noun = random.choice(nouns)
    alt += ran_noun
    alt +=" "
    ran_noun = random.choice(nouns)
    alt += ran_noun
    names.append(alt)
    alt = ""

#bokstaver
for _ in range (randint(5,15)):
    for i in range(randint(3,15)):
        if consec_cons >= 2:
            char = random.choice(vow + special)
            consec_cons = 0
            if char in vow:
                consec_vow += 1
        elif consec_vow <= 2:
            char = random.choice(cons + special)
            consec_vow = 0
            if char in cons:
                consec_cons +=1
        else:
            choice = random.choice(vow + cons + special)
            char = random.choice(choice)
            if char in cons:
                consec_cons += 1
                consec_vow = 0
            elif char in vow:
                consec_vow += 1
                consec_cons = 0

        alt += char
    names.append(alt)
    alt=""
def kingdomN():
    return random.choice(names)

#random.shuffle(names)
for item in names:
    print(item)

#If a is changed to w it will rewrite the file and delete the old results. a for append, w write.
with open('wordlists/namesSaved.txt', 'a') as file:
    for items in names:
        file.write(items + '\n')