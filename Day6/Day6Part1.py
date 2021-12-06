fishes = []
fish_ages = []


with open("Day6.txt", "r") as f:
    ages = f.readline().split(",")
    for v in ages:
        fish_ages.append(int(v))




class Fish:
    def __init__(self, age, new=False):
        self.age = age
        self.new = new

    def update(self):
        if self.age == 0:
            self.age = 6
            fishes.append(Fish(age=8, new=True))
        else:
            self.age -= 1


# initialise population
for age in fish_ages:
    fishes.append(Fish(age=age))

t = 0

while t < 80:
    for fish in fishes:
        if not fish.new:
            fish.update()
        else:
            fish.new = False
    t += 1
    print(t, len(fishes))

print(len(fishes))
