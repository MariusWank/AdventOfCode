import numpy as np

f = open("1stDayPart2.txt", "r")

scans = []
for line in f:
    scans.append(int(line.rstrip("\n")))

i = 1
counter = 0

# assuming 2 scans are always less than 3 scans
while i < (len(scans) - (len(scans)%3)):
    if np.sum([scans[i], scans[i+1], scans[i+2]]) > np.sum([scans[i-1], scans[i], scans[i+1]]):
        counter += 1
    i += 1



print(counter)