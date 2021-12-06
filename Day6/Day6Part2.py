
fish_ages = []
fishes = 9 * [0]


with open("Day6.txt", "r") as f:
    ages = f.readline().split(",")
    for v in ages:
        fish_ages.append(int(v))


for ages in fish_ages:
    fishes[ages] += 1


t = 0
new = 0
while t < 256:

    print(t, fishes)
    for i, group in enumerate(fishes):
        if i != 0:
            fishes[i - 1] = fishes[i]
        else:
            new = group
    fishes[6] += new
    fishes[8] = new
    t += 1



print(sum(fishes))

