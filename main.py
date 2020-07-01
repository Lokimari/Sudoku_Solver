# Create Game Board

def create_display():
    sudoku_row = []

    for space in range(0, 9):
        sudoku_row.append([None for x in range(0, 9)])

    return sudoku_row

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

