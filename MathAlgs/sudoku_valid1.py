def isValidSudoku(board):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != "."]
        return len(set(unit)) == len(unit)

    # Check rows
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*board):
        if not is_valid_unit(col):
            return False

    # Check 3x3 sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(sub_box):
                return False

    return True

sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

result = isValidSudoku(sudoku_board)
print(result)
