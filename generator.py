# Generate Sudoku Puzzles
import random

# Initialization #######################################################################################################

def create_board_array():
    sudoku_board = []

    for spot in range(0, 9):
        sudoku_board.append([None for spot in range(0, 9)])

    return sudoku_board

def set_sudoku_values(board_data):
    for row in range(len(board_data)):
        sudoku_nums = {num for num in range(1, 10)}
        for tile in range(len(board_data)):
            try:
                rand_num = random.randint(min(sudoku_nums), max(sudoku_nums))
                board_data[row][tile] = rand_num
            except ValueError:
                pass

    return board_data

# Tests ################################################################################################################

def test_rows(board_data):
    row_index = 3
    for x in range(len(board_data)):
        print(board_data[row_index][x])

def test_columns(board_data):
    column_index = 3
    for x in range(len(board_data)):
        print(board_data[x][column_index])

def test_3x3_box(board_data):
    # Box_ymax can be found by (box * 3) - 1
    # Box_ymin is just Box_ymax - 2

    # Box_x is as follows:
    # box = 1, 2, 3: x is 0, 1, or 2
    # box = 4, 5, 6: x is 3, 4, or 5
    # box = 7, 8, 9: x is 6, 7, or 8

    box = 8
    box_data = []

    x_range, y_range = get_ranges(box)

    print(f"y_range: {y_range}")

    print(f"x_range: {x_range}")

    box_data.append\
         ([board_data[x_range[0]][y_range[0]], board_data[x_range[0]][y_range[1]], board_data[x_range[0]][y_range[2]],
           board_data[x_range[1]][y_range[0]], board_data[x_range[1]][y_range[1]], board_data[x_range[1]][y_range[2]],
           board_data[x_range[2]][y_range[0]], board_data[x_range[2]][y_range[1]], board_data[x_range[2]][y_range[2]]])

    print(f"Box Data for box {box}: {box_data}")

# Getting index data ###################################################################################################

def get_ranges(box):
    x_range = []
    y_range = []
    # y_ranges
    if box == 1 or box == 4 or box == 7:
        y_range = [0, 1, 2]

    elif box == 2 or box == 5 or box == 8:
        y_range = [3, 4, 5]

    elif box == 3 or box == 6 or box == 9:
        y_range = [6, 7, 8]

    # x_ranges
    if box == 1 or box == 2 or box == 3:
        x_range = [0, 1, 2]

    elif box == 4 or box == 5 or box == 6:
        x_range = [3, 4, 5]

    elif box == 7 or box == 8 or box == 9:
        x_range = [6, 7, 8]

    return x_range, y_range

def get_box(x, y):
    if x in range(0, 3) and y in range(0, 3):
        return 1
    elif x in range(0, 3) and y in range(3, 6):
        return 2
    elif x in range(0, 3) and y in range(6, 9):
        return 3
    elif x in range(3, 6) and y in range(0, 3):
        return 4
    elif x in range(3, 6) and y in range(3, 6):
        return 5
    elif x in range(3, 6) and y in range(6, 9):
        return 6
    elif x in range(6, 9) and y in range(0, 3):
        return 7
    elif x in range(6, 9) and y in range(3, 6):
        return 8
    elif x in range(6, 9) and y in range(6, 9):
        return 9

# Duplication removal ##################################################################################################

def remove_dupes_in_column(board_data, column):
    column_to_fix = column

    for tile in range(len(board_data[column_to_fix])):
        current_num = board_data[tile][column_to_fix]

        for num in range(len(board_data[column_to_fix])):
            if current_num == board_data[num][column_to_fix] and tile != num:
                board_data[num][column_to_fix] = 0

def remove_dupes_in_row(board_data, row):
    row_to_fix = row

    for tile in range(len(board_data[row_to_fix])):
        current_num = board_data[row_to_fix][tile]

        for num in range(len(board_data[row_to_fix])):
            if current_num == board_data[row_to_fix][num] and tile != num:
                board_data[row_to_fix][num] = 0

def remove_dupes_in_box(board_data, box):
    x_range, y_range = get_ranges(box)

    for x in x_range:
        for y in y_range:
            current_num = board_data[x][y]

            for x_num in x_range:
                for y_num in y_range:
                    if current_num == board_data[x_num][y_num] and (x != x_num and y != y_num):
                        board_data[x_num][y_num] = 0