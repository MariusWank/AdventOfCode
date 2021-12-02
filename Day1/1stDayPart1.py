f = open("1stDayPart1.txt", "r")

scans = []
for line in f:
    scans.append(int(line.rstrip("\n")))

i = 1
counter = 0

while i < len(scans):
    if scans[i] > scans[i-1]:
        counter += 1
    i += 1

print(counter)