def create_board(width, height):
    return [
        ['#' if (i + j) % 2 == 0 else '*' for i in range(width)]
        for j in range(height)
    ]

board = create_board(4, 4)
for row in board:
    print(row)
    
# def chessboard(board):
#     return [
#         ['#' if cell == '#' else '$' for cell in row]
#         for row in board
#     ]

# new_board = chessboard(board)
# for row in new_board:
#     print(row)