# reading out data
with open("Day6.txt", "r") as f:
    fish_ages = []
    ages = f.readline().split(",")
    for v in ages:
        fish_ages.append(int(v))

# creating list of each fish age and adding fish according to their age
fish = 9 * [0]

for ages in fish_ages:
    fish[ages] += 1

# iterating days, refreshing numbers per group and adding new fish/resetting fish that replicated
t = 0

while t < 256:
    for i, group in enumerate(fish):
        if i != 0:
            fish[i - 1] = fish[i]
        else:
            new = group # saves value of fish[0] to add new fish and reset fish that replicated to 6
    fish[6] += new
    fish[8] = new
    t += 1

print(sum(fish))

