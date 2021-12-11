# collecting data
lines = []

with open("Day10.txt", "r") as f:
    for line in f:
        lines.append(line.rstrip("\n"))

# defining scores and characters used
open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]
points = [3, 57, 1197, 25137]
auto_value = [1, 2, 3, 4]
corrupt_score = 0
auto_scores = []
missing_seq = []

# iterating each character of each line until corrupted character is found or line is over
for line in lines:
    expected = ["N"]    # last entry represents expected character if it is not an "open-character"
    missing = ""    # stores missing sequence of incomplete lines
    stop = False    # early stopping variable if line is corrupted

    # iterating each character
    for x, char in enumerate(line):

        # if character is an "open-character" it's counter part is expected next
        for i, o in enumerate(open):
            if char == o:
                expected.append(close[i])
                break

        # if character is an "close-character" and is expected, last entry of expected gets removed
        for j, c in enumerate(close):
            if char == c:
                if char in expected[-1]:
                    expected.pop()
                    break

                # if character is not expected we add points according to character
                else:
                    corrupt_score += points[j]
                    stop = True
                    break
        if stop:
            break

    # if line is not corrupted and we still have characters in the expected list we add them to a new list
    while expected[-1] != "N" and not stop:
        missing += expected.pop()
    if not stop:
        missing_seq.append(missing)

# calculating scores for the missing sequences
for seq in missing_seq:
    score = 0
    print(seq)
    for c in seq:
        score *= 5
        score += auto_value[close.index(c)]
    print(score)
    auto_scores.append(score)

# printing results
print(corrupt_score)
print(sorted(auto_scores)[int((len(auto_scores)/2))])