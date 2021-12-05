boards = []

with open("4thDay.txt", "r") as f:
    board = []
    for i, line in enumerate(f):
        if line == "\n":
            boards.append(board)
            board = []
            continue
        row = list(filter(None, line.rstrip("\n").split(" ")))
        board.append(row)

# first row of file is bingo input sequence
inputs = boards[0][0][0].split(",")

# deleting input since var should only store boards
del boards[0]


# getting rows and columns of board
def generate_r_c(boards):
    rows = []
    columns = []
    for k, board in enumerate(boards):
        for i, row in enumerate(board):
            rows.append(row)
            if i % len(row) == 0 or i == 0:
                t = 0
                while t < 5:
                    columns.append([])
                    t += 1
            for j, v in enumerate(row):
                columns[j + (k * len(row))].append(v)
    return [rows, columns]




# checking which row/column won and deleting winners
sequence = []
last_loser_idx = []

for v in inputs:
    del_idx = []
    sequence.append(v)
    rows, columns = generate_r_c(boards)
    print(len(boards))
    for r in rows:
        if set(r).issubset(sequence):
            winner_idx = rows.index(r)
            del_idx.append(int(winner_idx / len(row)))
    for c in columns:
        if set(c).issubset(sequence):
            winner_idx = columns.index(c)
            del_idx.append(int(winner_idx / len(row)))
    del_idx = sorted(list(set(del_idx)), reverse=True)
    for idx in del_idx:
        if len(boards) != 1:
            del boards[idx]
        else:   # if we have one board left we have to continue the sequence until it wins
            if len(del_idx) == 1:
                last_loser_idx.append(idx)
                break
    if len(last_loser_idx) == 1:
        break


print(boards)

# adding values of board that are not in sequence
summe = 0
for n in boards[0]:
    for m in n:
        if m not in sequence:
            summe += int(m)

# multiplying sum with last input number to get result
result = summe * int(sequence[-1])

print(result)
