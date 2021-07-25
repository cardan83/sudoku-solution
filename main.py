# import numpy as np
import copy
import math

sudoku_original = [
    [0, 0, 6, 2, 0, 0, 0, 0, 7],
    [0, 9, 0, 7, 0, 6, 0, 3, 0],
    [5, 0, 0, 0, 8, 4, 0, 0, 0],
    [1, 0, 8, 3, 0, 0, 0, 5, 0],
    [0, 0, 5, 0, 0, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 5, 1, 0, 4],
    [0, 0, 0, 4, 9, 0, 0, 0, 6],
    [0, 8, 0, 0, 0, 7, 0, 1, 0],
    [7, 0, 0, 0, 0, 1, 8, 0, 0]
]
sudoku_2 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
sudoku = sudoku_2
# sudoku = sudoku_original

# sudoku = [
#     [3, 0, 4, 0],
#     [0, 1, 0, 2],
#     [0, 4, 0, 3],
#     [2, 0, 1, 0]
# ]

size = len(sudoku[0])


def print_sudoku():
    print('sudoku')
    for i in range(size):
        print(sudoku[i])


def pos_nrs_row(row_nr):
    global sudoku
    pos_nrs_row_list = []
    for i in range(size):
        if sudoku[row_nr].count(i+1) == 0:
            pos_nrs_row_list.append(i+1)
    # print('pos_nrs_row_list', pos_nrs_row_list)
    return pos_nrs_row_list


def pos_nrs_col(col_nr):
    global sudoku
    col_list = []
    for i in range(size):
        col_list.append(sudoku[i][col_nr])
    # print('col_list', col_list)
    pos_nrs_col_list = []
    for i in range(size):
        if col_list.count(i + 1) == 0:
            pos_nrs_col_list.append(i + 1)
    # print('pos_nrs_col_list', pos_nrs_col_list)
    return pos_nrs_col_list


def pos_nrs_squ(row_nr, col_nr):
    global sudoku
    square_size = int(math.sqrt(size))
    mod_res_row = row_nr % square_size
    mod_res_col = col_nr % square_size
    start_row = row_nr - mod_res_row
    start_col = col_nr - mod_res_col
    # print('start_row', start_row)
    # print('start_col', start_col)
    squ_list = []
    pos_nrs_squ_list = []
    for i in range(square_size):
        for j in range(square_size):
            squ_list.append(sudoku[start_row + i][start_col + j])
    for i in range(size):
        if squ_list.count(i + 1) == 0:
            pos_nrs_squ_list.append(i + 1)
    return pos_nrs_squ_list


def find_nrs(sud):
    for i in range(size):
        for j in range(size):
            if sud[i][j] == 0:
                pos_nrs = list(set(pos_nrs_row(i)) & set(pos_nrs_col(j)) & set(pos_nrs_squ(i, j)))
                # print(f'pos_nrs --- i{i} j{j} ---', pos_nrs)
                if len(pos_nrs) == 1:
                    sud[i][j] = pos_nrs[0]
    return sud


def solved():
    global sudoku
    result = False
    full_list = []
    for i in range(size):
        full_list = full_list + sudoku[i]
    if full_list.count(0) == 0:
        result = True
    return result


if __name__ == '__main__':
    print_sudoku()
    loop = 0
    chance_nr = 1
    while not solved():
        sudoku = copy.deepcopy(sudoku_2)
        sudoku[0][2] = chance_nr
        for i in range(100):
            sudoku = find_nrs(sudoku)
            loop += 1
            print('loop', loop)
            print_sudoku()
            if solved():
                break
        chance_nr += 1
