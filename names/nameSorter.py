names = []
surname = []

with open('../names/wordlists/AllTogether.txt', 'r') as file:
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


with open('../names/wordlists/names.txt', 'a') as file:
    for item in names:
        file.write(item +'\n')
with open('../names/wordlists/surnames.txt', 'a') as file:
    for item in surname:
        file.write(item +'\n')
with open('../names/wordlists/AllTogether.txt', 'w') as file:
        file.write('')