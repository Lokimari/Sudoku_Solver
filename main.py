import random

def create_board_array():
    sudoku_board = []

    for spot in range(0, 9):
        sudoku_board.append([None for spot in range(0, 9)])

    return sudoku_board

def display_board(board_data):
    row_counter = 0

    for row in board_data:
        column_counter = 0

        if row_counter == 3 or row_counter == 6:
            print("\n" + str(row))

        else:
            print(str(row))

        row_counter += 1

def set_sudoku_values(board_data):
    for row in range(len(board_data)):
        sudoku_nums = [num for num in range(1, 10)]
        for tile in range(len(board_data)):
            try:
                rand_num = random.randint(min(sudoku_nums), max(sudoku_nums))
                board_data[row][tile] = rand_num
                sudoku_nums.remove(rand_num)
            except ValueError:
                pass

    return board_data

def test_rows(board_data):
    row_index = 3
    for x in range(len(board_data)):
        print(board_data[row_index][x])

def test_columns(board_data):
    column_index = 3
    for x in range(len(board_data)):
        print(board_data[x][column_index])

def test_3x3_box(board_data):
    # Box 1 is
    # 0, 0 - 0, 1 - 0, 2
    # 1, 0 - 1, 1 - 1, 2
    # 2, 0 - 2, 1 - 2, 2

    # Box_ymax can be found by (box * 3) - 1
    # Box_ymin is just Box_ymax - 2

    # Box_x is as follows:
    # box = 1, 2, 3: x is 0, 1, or 2
    # box = 4, 5, 6: x is 3, 4, or 5
    # box = 7, 8, 9: x is 6, 7, or 8

    box_data = []

    box = 7

    if box == 1 or box == 4 or box == 7:
        y_range = [0, 1, 2]

    elif box == 2 or box == 5 or box == 8:
        y_range = [3, 4, 5]

    elif box == 3 or box == 6 or box == 9:
        y_range = [6, 7, 8]

    print(f"y_range: {y_range}")

    if box == 1 or box == 2 or box == 3:
        x_range = [0, 1, 2]

    elif box == 4 or box == 5 or box == 6:
        x_range = [3, 4, 5]

    elif box == 7 or box == 8 or box == 9:
        x_range = [6, 7, 8]

    print(f"x_range: {x_range}")

    box_data.append\
         ([board_data[x_range[0]][y_range[0]], board_data[x_range[0]][y_range[1]], board_data[x_range[0]][y_range[2]],
           board_data[x_range[1]][y_range[0]], board_data[x_range[1]][y_range[1]], board_data[x_range[1]][y_range[2]],
           board_data[x_range[2]][y_range[0]], board_data[x_range[2]][y_range[1]], board_data[x_range[2]][y_range[2]]])

    print(f"Box Data for box {box}: {box_data}")

def main():
    board_data = create_board_array()
    board_data = set_sudoku_values(board_data)

    # test_rows(board_data)
    # test_columns(board_data)
    test_3x3_box(board_data)

    display_board(board_data)


if __name__ == "__main__":
    main()
