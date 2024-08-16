# Load chess board coordinates into board_pos dictionary
board_pos = {}
columns = 'abcdefgh'
rows = '87654321'
for i in range(8):
    for j in range(8):
        board_pos[(i, j)] = columns[j] + rows[i]