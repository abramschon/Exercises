import random as rnd
import os

names = ["Bram", "Josephine", "Ziga", "Joana", "Lukas", "Kirsty", "Chloe"]
n = len(names)
present_ord = list(range(n)) #order in which names are shown

#shuffle names and the order they are shown 
rnd.shuffle(names)
rnd.shuffle(present_ord)

for i in present_ord:
    input(f"Please call: {names[i]}\n Press press enter ONLY if you are {names[i]}\n")
    input(f"Your target is: {names[(i+1)%n]}\n Press enter to clear and then call next person\n") 
    os.system('clear')

