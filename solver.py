# Solve Sudoku Puzzles

solvable_puzzle = [
    [1, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 4, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 5, 3, 0, 6, 0],
    [0, 6, 0, 3, 0, 0, 2, 0, 0],
    [0, 0, 4, 0, 1, 0, 8, 0, 0],
    [0, 0, 9, 0, 0, 5, 0, 1, 0],
    [4, 9, 5, 2, 7, 0, 0, 0, 0],
    [7, 0, 0, 5, 0, 9, 0, 4, 0],
    [6, 0, 0, 0, 3, 0, 0, 0, 5]
]


def display_board(board_data):
    print("         Sudoku")
    board_display = ""

    for row in range(len(board_data)):
        this_row = ""

        for tile in range(len(board_data[row])):

            if tile == 2 or tile == 5:
                this_row += " " + str(board_data[row][tile]) + "] ["
            elif tile == 0 or tile == 3 or tile == 6:
                this_row += str(board_data[row][tile])
            else:
                this_row += " " + str(board_data[row][tile])

        board_display += "[" + this_row + "]" + "\n"

        if row == 2 or row == 5 or row == 8:
            board_display += "\n"
        else:
            pass

    print(board_display)

# Following code stolen from https://www.youtube.com/watch?v=G_UYXzGuqvM
# Things stolen: simplification of possible() function, some of the solve() logic, printing board in the function :P

def possible(x, y, n):
    for i in range(0, 9):
        if solvable_puzzle[x][i] == n:
            return False
        if solvable_puzzle[i][y] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for i2 in range(0, 3):
            if solvable_puzzle[x0 + i][y0 + i2] == n:
                return False
    return True

def solve():
    global solution_count
    global solvable_puzzle
    for x in range(9):
        for y in range(9):
            if solvable_puzzle[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        solvable_puzzle[x][y] = n
                        solve()
                        solvable_puzzle[x][y] = 0
                return
    display_board(solvable_puzzle)
    question = input("Seek others?")
    solution_count += 1


def solver():
    display_board(solvable_puzzle)
    solve()
    print(f"{solution_count} total solutions.")


solver()
