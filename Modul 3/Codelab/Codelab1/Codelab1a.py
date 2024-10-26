def create_chessboard(width, height):
    return [['x' if (i + j) % 2 == 0 else 'o' for j in range(width)] for i in range(height)]

width = 6
height = 4
chessboard = create_chessboard(width, height)
for row in chessboard:
    print(row)
