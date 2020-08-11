import random

def create_board_array():
    sudoku_board = []

    for spot in range(0, 9):
        sudoku_board.append([None for spot in range(0, 9)])

    return sudoku_board

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

def set_sudoku_values(board_data):
    for row in range(len(board_data)):
        sudoku_nums = {num for num in range(1, 10)}
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

    x_range, y_range = get_ranges(box)

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

# def assign_row_via_set(board_data, row):
#     row_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#
#     for tile in range(len(board_data[row])):
#         board_data[row][tile] = random.randint(min(row_set), max(row_set))

def solve(board_data, x, y, n):
    if board_data[x][y] == 0:

        if n not in board_data[x]:

            column_tiles = []
            for column_tile in range(len(board_data)):
                column_tiles.append(board_data[column_tile][y])

            if n not in column_tiles:
                print(f"{n} not in row/column...")

                box = get_box(x, y)
                x_range, y_range = get_ranges(box)

                box_nums = []
                for xnum in x_range:
                    for ynum in y_range:
                        box_nums.append(board_data[xnum][ynum])

                if n not in box_nums:
                    print(f"Valid: {n} entered at {x, y}")
                    board_data[x][y] = n
            else:
                print(f"{n} not available at {x, y}")

        else:
            print(f"{n} not available at {x, y}")

    else:
        print("space occupied...")


def main():
    board_data = create_board_array()
    board_data = set_sudoku_values(board_data)

    # test_rows(board_data)
    # test_columns(board_data)
    test_3x3_box(board_data)

    display_board(board_data)
    print("############################")

    for num in range(0, 9):
        remove_dupes_in_column(board_data, num)
        remove_dupes_in_row(board_data, num)
        remove_dupes_in_box(board_data, num + 1)

    display_board(board_data)


if __name__ == "__main__":
    main()
