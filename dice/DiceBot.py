from random import *
import discord
import os

client = discord.client()

async def on_message(message):
    if message.author == client.user:
        return

diceSet = [2, 4, 6, 8, 10, 12, 20]
diceString=input("Hvor mange og hvilken terning? skriv i formen 2d6, der 2 er antall terninger, og d6 er terningen:")

antall, terning = diceString.split('d')
amount=int(antall)
dice=int(terning)
print(amount, dice)
res = []
for _ in range(amount):
    if dice in diceSet:
        res.append(randint(1, dice))
    else:
        print("Eksisterer ikke, prøv på nytt.")
added = 0
ant = [int(x) for x in res] #makes the res into int
for i in range(len(res)): #counting the variables
    added += ant[i]
    print(i, ant[i], added)

print(res, added)

