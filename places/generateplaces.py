from random import randint
import random
#Generate towns and villages,city by inputting what type of area is needed.
print("YOU choose what place you are visiting. Your options are: Village, town, city, or capital. if you leave it blank, it chooses a random.")
type = input("What are you visiting?")
# Define different places:
#Villages, up to 1000 inhabitants, around 13 square miles, 1 box is a mile

if type == '':
    type = random.choice(['village', 'town', 'city'])


#Buildings
empty = ['0']
shops = ['Smith','general shop','carpenter','tanner','tailor','shoemaker', 'chandler','Smithy', 'weaver','leatherworker','market','0']
sleep = ['Home','Inn','stable','bathhouse','0']
fd = ['tavern','bar', 'restaurant','cafe','bakery','butcher','fisher', 'brewer', 'cheesemaker', 'woodworker','0']
edu = ['school','library','schoolhouse','academy','college','museum','0']
magic = ['wizardtower','healer clinic','0']
safety = ['fortress','watchtower','fire station','bailiff','sheriff','jail','Guardhouse','Militia Barracks','0']
water = ['well','river','glacier','0']
factories = ['coalmines','saltmines','mill','goldmines','mines','lab']
other = ['castle','Townhall','post office','hospital','bank','Monument','0']
government = ['autocracy','beureacracy','confederacy','democracy','dictatorship','feudalism','gerontocracy','hierarchy','magocracy','matriarchy','militocracy','monocracy','oligarchy','patriarchy','meritogracy','plutocracy','republic','satrapy','kleptocracy','theocracy']
atmosphere = ['Foggy','humid','dry','sunny','snow','cloudy','grey','rain','windy']

grid = []
build = []
col = 0
rows = 0
spots = 0

#village
if type.startswith('V') or type.startswith('v'):
    col = randint(2, 3)
    rows = randint(3, 5)
    spots = col*rows
    population = randint(100, 1100)
    '''print(col,rows)
    print(build, spots)'''
#town
elif type.startswith('t') or type.startswith('T'):
    col = randint(2,6)
    rows = randint(6,9)
    spots = col * rows
    population = randint(1500, 6300)
    '''print(build, spots)
    print(col, rows)'''
#city
elif type.startswith('c') or type.startswith('C'):
    citizens = randint(6500, 50000)
    if citizens < 12000:
        city = 'small'
        rows = randint(7, 9)
        col = randint(8, 15)
    elif 1200< citizens <25000:
        city = 'medium'
        rows = randint(8, 10)
        col = randint(8, 16)
    else:
        city = 'big'
        rows = randint(9, 12)
        col = randint(8, 17)
    population = citizens
    spots = col * rows
    '''print(city, col, rows)
    print(build, spots)'''

if type == 'city':
    print("You have arrived at a ", city, type)
else:
    print("You have arrived at a ",type)
print('with a population of:', population,' inhabitants')
print('it is a ',random.choice(atmosphere),'day', 'in the ',random.choice(government),'governed',type)

#making list
for _ in range(spots):
    randList = random.choice([empty, shops, sleep, fd, edu, magic, safety,factories, water, other])
    build.append(random.choice(randList))

#making the grid
random.shuffle(build)
grid = [build[i:i+col]for i in range(0,rows*col, col)]
#grid = [[build for _ in range(col)] for _ in range(rows)]
print('the ', type,' is built with these things in them:')

for row in grid:
    print(row)

print('The atmosphere around is:', random.choice(atmosphere),' and is governed by:', random.choice(government))