"""
The main module of puzzle.
https://github.com/MykhailoSobko/puzzle
"""

def check_rows(board: list) -> bool:
    """
    Check whether the numbers in the rows are from 1 to 9 and unique.

    >>> check_rows([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    True
    """
    for row in board:
        numbers = set()
        for cell in row:
            if cell.isnumeric():
                cell = int(cell)
                if cell not in range(1, 10):
                    return False
                if cell not in numbers:
                    numbers.add(cell)
                else:
                    return False

    return True


def check_columns(board: list) -> bool:
    """
    Check whether the numbers in the columns are from 1 to 9 and
    unique.

    >>> check_columns([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    """
    for j in range(9):
        numbers = set()
        for i in range(9):
            if board[i][j].isnumeric():
                cell = int(board[i][j])
                if cell not in range(1, 10):
                    return False
                if cell not in numbers:
                    numbers.add(cell)
                else:
                    return False

    return True


def check_colors(board: list) -> bool:
    """
    Check whether the numbers in the blocks of color are from 1 to 9 and
    unique.

    >>> check_colors([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    True
    """
    for pivot in range(5):
        numbers = set()
        i = 8-pivot
        for j in range(pivot, pivot+5):
            if board[i][j].isnumeric():
                cell = int(board[i][j])
                if cell not in range(1, 10):
                    return False
                if cell not in numbers:
                    numbers.add(cell)
                else:
                    return False

        j = pivot
        for i in range(7-pivot, 3-pivot, -1):
            if board[i][j].isnumeric():
                cell = int(board[i][j])
                if cell not in range(1, 10):
                    return False
                if cell not in numbers:
                    numbers.add(cell)
                else:
                    return False

    return True


def validate_board(board: list) -> bool:
    """
    Validate the board ready for the game.

    >>> validate_board([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    """
    return (check_rows(board)
        and check_columns(board)
        and check_colors(board)
        )
