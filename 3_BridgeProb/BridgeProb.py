import math
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations as perm

cards = np.tile(np.arange(1,14),4)

# shuffle cards
n = 100000
counts = np.zeros(5) #for counting how many times 0, 1, 2, 3, 4 aces pop up

for i in range(n):
    np.random.shuffle(cards)

    # take the first 13 cards and count the aces, represented as ones
    count = sum(cards[:13]==1)
    counts[count] +=1

print(counts/n)

probs = np.array([
    39*38*37*36,
    39*38*37*13*4,
    39*38*13*12*6,
    39*13*12*11*4,
    13*12*11*10
]) / (52*51*50*49)

print(probs)

