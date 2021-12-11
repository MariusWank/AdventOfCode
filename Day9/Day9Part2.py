# collecting data and adding padding
lines = []
with open("Day9.txt", "r") as f:
    for line in f:
        length = len(line)
        lines.append(line.rstrip("\n"))
    lines.append("9" * length)
    lines.insert(0, "9" * length)

for i, line in enumerate(lines):
    line = "9" + line
    line += "9"
    lines[i] = line

# collecting lowest points and calculating basins
basins = []
for i, line in enumerate(lines):
    for j, n in enumerate(line):
        if i != 0 and i != len(lines) - 1 and j != 0 and j != len(line) - 1:
            if lines[i + 1][j] > n and lines[i - 1][j] > n and line[j + 1] > n and line[j - 1] > n:
                basin = [[i, j]]
                if basin[0] in basins:
                    break
                for coords in basin:
                    [x, y] = coords
                    if x != 0 and x != len(lines) - 1 and y != 0 and y != len(line) - 1:
                        for neighbour in [[x, y - 1], [x, y + 1], [x + 1, y], [x - 1, y]]:
                            if int(lines[neighbour[0]][neighbour[1]]) != 9 and neighbour not in basin:
                                basin.append(neighbour)
                basins.append(basin)

# calculating basin sizes
basin_sizes = []

for b in basins:
    basin_sizes.append(len(b))

# multiplying 3 largest basin sizes
prod = 1
for b in sorted(basin_sizes)[-3:]:
    prod *= b

print(prod)
