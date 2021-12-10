import numpy as np

puzzle_dic  ={}

with open("Day8.txt", "r") as f:
    for line in f:
        ent, out = line.rstrip("\n").split(" | ")
        puzzle_dic[ent] = out

# encoding numbers: index = segment state
numbers = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1],
           [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]

segments = ["a", "b", "c", "d", "e", "f", "g"]

seg_to_idx = {}
for i, seg in enumerate(segments):
    seg_to_idx[seg] = i


counter = 0
true_numbers = []
Part1 = False
for key in puzzle_dic:

    # setting up wiring dic and puzzle input
    wiring = {} # letter -> segment letter (like original)
    entries = [e for e in key.split(" ")]
    outputs = [o for o in puzzle_dic[key].split(" ")]
    ZeroSixNine = []
    TwoFiveThree = []

    # defining which code corresponds to which number
    for entry in entries:
        if len(entry) == 2:
            one = entry
        elif len(entry) == 3:
            seven = entry
        elif len(entry) == 4:
            four = entry
        elif len(entry) == 7:
            eight = entry
        elif len(entry) == 6:
            ZeroSixNine.append(entry)
        else:
            TwoFiveThree.append(entry)

    # creating list of all code-numbers
    num_list = [one, seven, four, eight]
    for n in TwoFiveThree:
        num_list.append(n)
    for n in ZeroSixNine:
        num_list.append(n)

    # finding out wiring for wire a to unknown segment
    for char in seven:
        if char not in one:
            wiring[char] = "a"

    # finding out wiring for wire f to unknown segment and finding out number two
    for num in TwoFiveThree:
        copy_num_list = [n for i, n in enumerate(num_list) if i != num_list.index(num)]
        count = 7 * [0]
        for i, c in enumerate(segments):
            for n in copy_num_list:
                for char in n:
                    if char == c:
                        count[i] += 1
                        if count[i] == 9:
                            wiring[c] = "f"
        if 9 in count:
            two = num

    # finding out wire e to unknown segment
    del TwoFiveThree[TwoFiveThree.index(two)]
    for char in two:
        if char not in TwoFiveThree[0] and char not in TwoFiveThree[1]:
            wiring[char] = "e"

    # finding out wire c to unknown segment
    for char in one:
        if char not in wiring.keys(): # richtig???
            wiring[char] = "c"

    # finding out wire d to unknown segment and finding out number Zero
    for num in ZeroSixNine:
        for c in segments:
            if c not in num and c not in wiring.keys(): # richtig???
                wiring[c] = "d"
                zero = num

    # finding out wire b to unknown segment
    for c in four:
        if c not in wiring.keys(): # richtig???
            wiring[c] = "b"

    # finding out wire g to unknown segment
    for c in eight:
        if c not in wiring.keys(): # richtig???
            wiring[c] = "g"

    # calculating puzzle result
    added_num = ""
    for num in puzzle_dic[key].split(" "):
        bin_num = [0] * 7
        trans_num = ""
        for c in num:
            trans_num += wiring[c]
        for c in trans_num:
            bin_num[seg_to_idx[c]] += 1
        true_num = numbers.index(bin_num)
        if true_num in [1, 4, 7, 8] and Part1:
            counter += 1
        elif not Part1:
            added_num += str(true_num)

    if not Part1:
        true_numbers.append(int(added_num))

if Part1:
    print(counter)
else:
    print(sum(true_numbers))

