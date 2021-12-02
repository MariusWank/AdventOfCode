f = open("2ndDayPart1.txt", "r")

command = []
value = []

for line in f:
    c, v = line.split(" ")
    command.append(c)
    value.append(int(v))

depth = 0
horizontal = 0

for i in range(len(command)):
    if command[i][0] == "f":
        horizontal += value[i]
    elif command[i][0] == "u":
        depth -= value[i]
    else:
        depth += value[i]

print(depth * horizontal)

