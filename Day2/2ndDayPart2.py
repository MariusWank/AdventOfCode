f = open("2ndDayPart2.txt", "r")

command = []
value = []

for line in f:
    c, v = line.split(" ")
    command.append(c)
    value.append(int(v))

depth = 0
horizontal = 0
aim = 0

for i in range(len(command)):
    if command[i][0] == "f":
        horizontal += value[i]
        depth += aim * value[i]
    elif command[i][0] == "u":
        aim -= value[i]
    else:
        aim += value[i]

print(depth * horizontal)