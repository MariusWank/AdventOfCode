import numpy as np
strip = []

with open("3rdDay.txt", "r") as f:
    for line in f:
        for c in f:
            strip.append(c.rstrip("\n"))

    size = len(strip[1])
    max_num = len(strip)
    count = size * [0]

for i, v in enumerate(strip):
    for j, n in enumerate(v):
        if int(n) % 7 == 1:
            count[j] += 1

gamma = [0] * size
epsilon = [0] * size

for i, num in enumerate(count):
    if num > max_num/2:
        gamma[i] += 1
    else:
        epsilon[i] += 1

gamma.reverse()
epsilon.reverse()

gamma_dec = 0
epsilon_dec = 0

for i, g in enumerate(gamma):
    if g == 1:
        gamma_dec += 2**i

for i, e in enumerate(epsilon):
    if e == 1:
        epsilon_dec += 2**i

print(gamma_dec * epsilon_dec)