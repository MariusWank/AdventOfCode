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

# collecting lowest points and calculating risk sum
low_points = []
for i, line in enumerate(lines):
    for j, n in enumerate(line):
        if i != 0 and i != len(lines) - 1 and j != 0 and j != len(line) - 1:
            if lines[i + 1][j] > n and lines[i - 1][j] > n and line[j + 1] > n and line[j - 1] > n:
                low_points.append(int(n))

risk_level_sum = sum(low_points) + len(low_points)

print(risk_level_sum)