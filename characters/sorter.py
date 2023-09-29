'''with open('government.txt','r') as file:
    list = file.read().splitlines()
'''
names = []
surname = []

with open('../names/wordlists/surnames.txt', 'r') as file:
    for line in file:
        n, s = line.strip().split(' ')
        names.append(n)
        surname.append(s)
print(names)
print(surname)
names.sort()
surname.sort()
print(names)
print(surname)


with open('../names/wordlists/surnames.txt', 'w') as file:
    for item in surname:
        file.write(item +'\n')
