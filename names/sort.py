new = []
prev_item = None
remover = []
with open('wordlists/verbs.txt', 'r') as file:
    vb = file.read().splitlines()
print(len(vb))
print(vb)
copy = vb
for item in vb:
    if item != prev_item:
        new.append(item)
    else:
        remover.append(item)
    prev_item = item

vb = new
print(len(vb))
print(vb)
print(remover)

#Updates list
with open('wordlists/verbs.txt', 'w') as file:
    for item in vb:
        file.write(item + '\n')


