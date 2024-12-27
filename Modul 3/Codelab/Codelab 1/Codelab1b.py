def create_chessboard(width, height):
    return [['x' if (i + j) % 2 == 0 else 'o' for j in range(width)] for i in range(height)]

def ubah_simbol(x):
    if x == 'x':
        return '#'
    else:
        return '+'

def transform_pattern(board):
    return [list(map(ubah_simbol, row)) for row in board]

width = 6
height = 4
chessboard = create_chessboard(width, height)
transformed_board = transform_pattern(chessboard)

for row in transformed_board:
    print(row)
