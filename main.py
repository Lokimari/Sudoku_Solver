# Create Game Board

def create_board_array():
    sudoku_board = []

    for spot in range(0, 9):
        sudoku_board.append([None for spot in range(0, 9)])

    return sudoku_board

def display():
    sudoku_board = create_display()
    sudoku_visual_board = "           Sudoku"

    row_x = 0
    for row in sudoku_board:
        row_y = 0
        sudoku_visual_board += "\n" + "[ "

        for tile in row:
            if tile is None:
                sudoku_visual_board += "_ "
            else:
                sudoku_visual_board += str(tile) + " "

            row_y += 1
            if row_y == 3 or row_y == 6:
                sudoku_visual_board += "] [ "

        sudoku_visual_board += "]"

        row_x += 1
        if row_x == 3 or row_x == 6:
            sudoku_visual_board += "\n"

    print(sudoku_visual_board)


def main():
    display()


if __name__ == "__main__":
    main()

