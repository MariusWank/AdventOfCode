
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
            columns[j+(k*len(row))].append(v)

# checking which row/column won
winner = False
winner_seq = None
winner_type = None
sequence = []

for v in inputs:
    sequence.append(v)
    for r in rows:
        if set(r).issubset(sequence):
            winner = True
            winner_seq = r
            winner_type = "row"
            break
    for c in columns:
        if set(c).issubset(sequence):
            winner = True
            winner_seq = c
            winner_type = "column"
            break
    if winner:
        break

# checking which board belongs to winner row/column
if winner_type == "row":
    winner_idx = rows.index(winner_seq)
    winner_brd = int(winner_idx/len(row))
else:
    winner_idx = columns.index(winner_seq)
    winner_brd = int(winner_idx / len(row))

# adding values of board that are not in sequence
summe = 0
for n in boards[winner_brd]:
    for m in n:
        if m not in sequence:
            summe += int(m)

# multiplying sum with last input number to get result
result = summe * int(sequence[-1])


print(result)