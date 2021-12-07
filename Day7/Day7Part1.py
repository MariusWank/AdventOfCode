# reading out puzzle input
with open("Day7.txt", "r") as f:
    positions = f.readline().split(",")
    for i, e in enumerate(positions):
        positions[i] = int(e)

# saving highest position
max_pos = max(positions)

# calculating costs per position to change to new position
costs = []
for i, n in enumerate(range(0, max_pos)):
    costs.append([])
    for pos in positions:
        costs[i].append(abs(n-pos))

# calculating position with minimum cost
min_cost = sum(costs[0])

for i, cost in enumerate(costs):
    if sum(cost) < min_cost:
        min_cost = sum(cost)
        min_pos = i

print(min_cost)