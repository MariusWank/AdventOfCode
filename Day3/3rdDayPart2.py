import numpy as np
strip = []

with open("3rdDay.txt", "r") as f:
    for line in f:
        for c in f:
            strip.append(c.rstrip("\n"))

bit_criteria = 0
size = len(strip[0])
max_num = len(strip)
count_one = 0
stays = None
strip2 = []

while bit_criteria < size and max_num > 1:

    del_index = []

    # counting 1 in bit criteria position
    for i, v in enumerate(strip):
        if v[bit_criteria] == "1":
            count_one += 1

    # deciding deletion criteria
    if count_one < max_num/2:
        stays = "0"
    else:
        stays = "1"

    # deleting rows that don't fulfill criteria
    for i, v in enumerate(strip):
        if v[bit_criteria] != stays:
            del_index.append(i)
    for idx in sorted(del_index, reverse=True):
        if bit_criteria == 0:
            strip2.append(strip[idx])
        del strip[idx]

    # resetting variables to new list and new criteria
    bit_criteria += 1
    size = len(strip[0])
    max_num = len(strip)
    count_one = 0
    stays = None


bit_criteria = 1
size = len(strip2[0])
max_num = len(strip2)
count_one2 = 0
stays2 = None


while bit_criteria < size and max_num > 1:

    del_index = []

    # counting 1 in bit criteria position
    for i, v in enumerate(strip2):
        if v[bit_criteria] == "1":
            count_one2 += 1

    # deciding deletion criteria
    if count_one2 < max_num/2:
        stays2 = "1"
    else:
        stays2 = "0"

    # deleting rows that don't fulfill criteria
    for i, v in enumerate(strip2):
        if v[bit_criteria] != stays2:
            del_index.append(i)
    for idx in sorted(del_index, reverse=True):
        del strip2[idx]


    # resetting variables to new list and new criteria
    bit_criteria += 1
    size = len(strip2[0])
    max_num = len(strip2)
    count_one2 = 0
    stays2 = None

ox_rate = []
scrub_rate = []

for v, w in zip(strip[0], strip2[0]):
    ox_rate.append(v)
    scrub_rate.append(w)


ox_rate.reverse()
scrub_rate.reverse()

ox_rate_dec = 0
scrub_rate_dec = 0

for i, s1 in enumerate(ox_rate):
    if s1 == "1":
        ox_rate_dec += 2**i

for i, s2 in enumerate(scrub_rate):
    if s2 == "1":
        scrub_rate_dec += 2**i

print(ox_rate_dec, scrub_rate_dec)
print(ox_rate_dec * scrub_rate_dec)