# getting data
lines = []
with open("Day5.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n").replace(" -> ", ",").split(",")
        lines.append(line)

# saving dim of our field matrix
xmax = 0
ymax = 0

for line in lines:
    for i, v in enumerate(line):
        v = int(v)
        if (i+1) % 2 == 0:
            if v > ymax:
                ymax = v
        else:
            if v > xmax:
                xmax = v

# creating field matrix
c1 = 0

field = []

while c1 < xmax+1:
    field.append([])
    c1 += 1
for row in field:
    c2 = 0
    while c2 < ymax+1:
        row.append(0)
        c2 += 1

# filtering only horizontal/vertical lines
filter_idx = []
for i, line in enumerate(lines):
    if line[0] == line[2] or line[1] == line[3]:
        filter_idx.append(i)

filtered_lines = []
for idx in filter_idx:
    filtered_lines.append(lines[idx])

# creating "elongated" lines
elongated_lines = []
for i, line in enumerate(filtered_lines):
    for j, v in enumerate(line):
        line[j] = int(v)
    elongated_lines.append([])
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    x_idx = []
    y_idx = []
    if x1 != x2:
        if x1 < x2:
            step = 1
        else:
            step = -1
        for n in range(x1, x2+step, step):
            x_idx.append(n)
    else:
        x_idx.append(x1)

    if y1 != y2:
        if y1 < y2:
            step = 1
        else:
            step = -1
        for n in range(y1, y2+step, step):
            y_idx.append(n)
    else:
        y_idx.append(y1)
    elongated_lines[i].append(x_idx)
    elongated_lines[i].append(y_idx)




for line in elongated_lines:
    for x in line[0]:
        for y in line[1]:
            field[x][y] += 1


count = 0
for row in field:
    for col in row:
        if col >= 2:
            count += 1

print(count)
