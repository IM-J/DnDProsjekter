import random
from random import randint
#old
'''tot = 0
if tot < 2:
    print("Your ability modifier is -5")
    if tot in (2, 3):
        print("Your ability modifier is -4.")
    if tot in (4, 5):
        print("Your ability modifier is -3.")
    if tot in (6, 7):
        print("Your ability modifier is -2.")
    if tot in (8, 9):
        print("Your ability modifier is -1.")
    if tot in (10, 11):
        print("Your ability modifier is 0.")
    if tot in (12, 13):
        print("Your ability modifie is 1.")
    if tot in (14, 15):
        print("Your ability modifie is 2.")
    if tot in (16, 17):
        print("Your ability modifie is 3.")
    if tot in (18, 19):
        print("Your ability modifie is 4.")
    if tot in (20, 21):
        print("Your ability modifie is 5.")
    if tot in (22, 23):
        print("Your ability modifie is 6.")
    if tot in (24, 25):
        print("Your ability modifie is 7.")
    if tot in (26, 27):
        print("Your ability modifie is 8.")
    if tot in (28, 29):
        print("Your ability modifie is 9.")
    if tot in (30, 31):
        print("Your ability modifie is 10.")'''

races = ['dwarf', 'elf', 'halfling', 'human', 'gnome', 'tiefling', 'dragnoborn', 'aasimar', 'genasi','goliath','kenku', 'tabaxi', 'aarakocra', 'orc', 'firbolgs', 'lizardfolk', 'tortles', 'warforged', 'changeling', 'kalashtar', 'shifters', 'pelode', 'fairy', 'mermaid']
halfbreed_races = ['dwarf', 'elf', 'human', 'gnome', 'pelode', 'fairy', 'mermaid', 'orc', 'unknown']
halfbreed = False
classes = ['artificer','barbarian','bard','blood hunter','cleric','druid','fighter','monk','paladin','ranger','rogue','sage','sorcerer','warlock','wizard', 'mystic']
background = ['acolyte','anthropologist','archaeologist','astral drifter','athlete', 'celebrity','charlatan', 'city watcher','courtier','criminal/spy','entertainer','faceless','faction agent','failed merchant','far traveler','feylost','fisher','folk hero','gambler','gladiator','haunted one','hermit','inheritor','investigator','knight', 'lorehold student','mage','marine','mercenary veteran','noble','outlander','pirate','plaintiff','prismari student','cultist','rival intern','rune carver','sage','sailor','shipwright','simic scientist','smuggler','soldier','bounty hunter','urchin','tribe member']
tradgedies = ['shipwrecked', 'hunted','cursed', 'betrayal','exile','lost love', 'orpahn','cursed lineage','injustice', 'illness', 'memoryloss','failed','lost hope','natural disaster', 'disgrace','disowned','family dethrowned']
happiness = ['Happy childhood', 'loving family', 'rich', 'bestfriend', 'pet', 'Fame and acclaim', 'successful apprenticeship','noble heritage','close-knit community','saved by a hero','blessed','exploration and adventure','artistic pursuit','nomadic upbringing','diplomatic success','mentored youth','historic discovery']
traitsP = ['selfless','noble','ambitious','kind','affectionate','humble','polite','straightforward''animal lover', 'brave', 'responsible', 'honest','optimistic', 'diplomatic','comapssionate']
traitsB = ['violent', 'gambler', 'gluttonous', 'paranoid','selfish','jealous','impulsive', 'irrational','irresponsible', 'pesimistic','argumentative','vengeful','vindictive','hestitant','hostile','impatiant','desperate']
stats = ["str","dex","con","intg","wis","char"]
other_parent = ""
allignment_vertical = ['lawful','neutral','chaotic']
allignment_horizontal = ['good','neutral','evil']
combo = []
calling = []
bg = []
tradg = []
traits = []
for _ in range(2):
    rand_call = random.choice(classes)
    while rand_call in calling:
        rand_call = random.choice(classes)
    calling.append(rand_call)
print(calling)

for _ in range(14):
    rand_bg = random.choice(background)
    while rand_bg in bg:
        rand_bg = random.choice(background)
    bg.append(rand_bg)
print(bg)

for _ in range(3):
    tradgedy = random.choice(tradgedies)
    while tradgedy in tradg:
        tradgedy = random.choice(tradgedies)
    tradg.append(tradgedy)
print(tradg)

for _ in range(4):
    trait = random.choice(traitsP)
    while trait in traits:
        trait = random.choice(traitsP)
    traits.append(trait)
for _ in range(3):
    traitN = random.choice(traitsB)
    while traitN in traits:
        traitN = random.choice(traitsB)
    traits.append(traitN)

print(traits)