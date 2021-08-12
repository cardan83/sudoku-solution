import copy
import math
# import time
# import numpy as np


sudoku_nyteknik = [
    [0, 0, 6, 2, 0, 0, 0, 0, 7],
    [0, 9, 0, 7, 0, 0, 0, 3, 0],
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

sudoku_3 = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
]

sudoku_small = [
    [3, 0, 4, 0],
    [0, 1, 0, 2],
    [0, 4, 0, 3],
    [2, 0, 1, 0]
]

# current_sudoku_challenge = sudoku_nyteknik
current_sudoku_challenge = sudoku_2
# current_sudoku_challenge = sudoku_3
# current_sudoku_challenge = sudoku_small
sudoku = current_sudoku_challenge

size = len(sudoku[0])
ch_nr_1 = 0
ch_nr_2 = 0
ch_nr_3 = 0
ch_nrs = []
chance_nr_tot = 3


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


def zero_row():
    global sudoku
    for row in range(size):
        for col in range(size):
            if sudoku[row][col] == 0:
                return row
    return -1


def zero_col():
    global sudoku
    for row in range(size):
        for col in range(size):
            if sudoku[row][col] == 0:
                return col
    return -1


def chance_nr_1():
    global ch_nr_1
    if ch_nr_1 == 9:
        ch_nr_1 = 1
    else:
        ch_nr_1 += 1
    return ch_nr_1


def chance_nr_2():
    global ch_nr_1
    global ch_nr_2
    if ch_nr_1 == 1:
        ch_nr_2 += 1
    if ch_nr_1 == 1 and ch_nr_2 == 10:
        ch_nr_2 = 1
    return ch_nr_2


def chance_nr_3():
    global ch_nr_1
    global ch_nr_2
    global ch_nr_3
    if ch_nr_1 == 1 and ch_nr_2 == 1:
        ch_nr_3 += 1
    if ch_nr_1 == 1 and ch_nr_2 == 1 and ch_nr_3 == 10:
        ch_nr_3 = 1
    return ch_nr_3


def chance_nr(nr):
    global ch_nrs    # list
    global chance_nr_tot
    if len(ch_nrs) == 0:
        for i in range(chance_nr_tot):
            if i+1 != chance_nr_tot:
                ch_nrs.append(1)
            else:
                ch_nrs.append(0)
    try:
        if nr == 0 and ch_nrs[nr + 1] == 9 and ch_nrs[nr + 2] == 9:  # Rad 1
            ch_nrs[nr] = ch_nrs[nr] + 1
        # if nr == 0 and ch_nrs[nr] == 9:
        #     return -1
        if nr == 1 and ch_nrs[nr + 1] == 9:  # Rad 2
            ch_nrs[nr] = ch_nrs[nr] + 1
        if nr == 1 and ch_nrs[nr] == 10:
            ch_nrs[nr] = 1
    except IndexError:
        pass  # list index out of range
        # print('list index out of range')
    if nr == 2:  # Rad 3
        if ch_nrs[nr] == 9:
            ch_nrs[nr] = 1
        else:
            ch_nrs[nr] = ch_nrs[nr] + 1
    return ch_nrs[nr]


if __name__ == '__main__':
    # print_sudoku()
    loop = 0
    for k in range(0):
        sudoku = find_nrs(sudoku)
        loop += 1
        print('loop', loop)
        print_sudoku()
        if solved():
            break
    while not solved():
        sudoku = copy.deepcopy(current_sudoku_challenge)
        for k in range(chance_nr_tot):
            sudoku[zero_row()][zero_col()] = chance_nr(k)
        for k in range(10):
            sudoku = find_nrs(sudoku)
            loop += 1
            print('loop', loop)
            print_sudoku()
            if solved():
                break
