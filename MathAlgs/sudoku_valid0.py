def check_unit(unit):
    """
    Checks if a row, column, or sub-box contains the digits 1-9 without repetition.

    Args:
      unit: A list of 9 elements representing a row, column, or sub-box of the Sudoku board.

    Returns:
      True if the unit is valid, False otherwise.
    """
    seen = set()
    for elem in unit:
        if elem == ".":
            continue
        num = int(elem)
        if num <= 0 or num > 9 or num in seen:
            return False
        seen.add(num)
    return True

def is_valid_sudoku(board):
    """
    Determines if a 9x9 Sudoku board is valid.

    Args:
      board: A 9x9 list of lists, where each inner list represents a row of the Sudoku board.

    Returns:
      True if the board is valid, False otherwise.
    """

    # Check rows.
    for row in board:
        if not check_unit(row):
            return False

    # Check columns.
    for col in range(9):
        column = [row[col] for row in board]
        if not check_unit(column):
            return False

    # Check 3x3 sub-boxes.
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[i + k][j + l] for k in range(3) for l in range(3)]
            if not check_unit(sub_box):
                return False

    return True

# Example usage:
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

if is_valid_sudoku(sudoku_board):
    print("The Sudoku board is valid.")
else:
    print("The Sudoku board is invalid.")
