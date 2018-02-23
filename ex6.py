#!/usr/bin/env python3
"""ex6.py
Author: Omar Amr
Matr.Nr.: K11776960
Exercise 6
"""

from ex5 import read_input_file
from ex5 import visualize_board
import numpy as np


def switch_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


def check_if_successive(item):
    if len(item) < 4:
        return False

    counter = 1
    for x in range(1, len(item)):
        if item[x] - item[x - 1] == 1:
            counter += 1
            if counter == 4:
                return True
        else:
            counter = 1

    return False


def check_game_status(board, columns, rows, turn):
    turn = str(turn)
    board1 = np.flip(np.transpose(board), 0)
    board2 = np.flip(board1, -1)
    status = [False, False, False]  # [Game over, P1 won, P2 won]

    for column in np.array(board):
        x = np.nonzero(column == turn)[0]
        if check_if_successive(x):
            status[int(turn)] = True
            return status

    for row in board1:
        x = np.nonzero(row == turn)[0]
        if check_if_successive(x):
            status[int(turn)] = True
            return status

    for counter in range(-1 * rows + 1, columns):
        diagonal1 = np.diag(board1, counter)
        diagonal2 = np.diag(board2, counter)
        x = np.nonzero(diagonal1 == turn)[0]
        y = np.nonzero(diagonal2 == turn)[0]
        if check_if_successive(x) or check_if_successive(y):
            status[int(turn)] = True
            return status

    empty_counter = 0
    for column in board:  # Check of all entries are full
        empty = [e for e in column if e == "NULL"]
        empty_counter += len(empty)

    if empty_counter == 0:
        status[0] = True
        return status

    return status


def draw_board(game_entries, columns_number, p1_symbol, p2_symbol, symbol_size):
    game_entries = np.flip(np.transpose(game_entries), 0)
    visualization_board = []

    for row in game_entries:
        for counter in range(symbol_size):
            line = ""
            for item in row:
                if item != "NULL":
                    if item == '1':
                        line += p1_symbol[counter]
                    else:
                        line += p2_symbol[counter]
                else:
                    line += " " * symbol_size

            visualization_board.append(line)

    return visualize_board(visualization_board, columns_number, symbol_size)


def play(config_file):
    board, p1_symbol, p2_symbol, columns_number, rows_number = read_input_file(config_file)
    game_over, p1_won, p2_won = [False, False, False]
    turn = 1
    final_state = ""

    game_entries = [["NULL" for x in range(rows_number)] for y in range(columns_number)]  # array list of each column

    while not (game_over or p1_won or p2_won):
        valid_column = False
        while not valid_column:
            try:
                input_type = -3
                input_column = int(input("Player's {} turn: ".format(turn)))
                if input_column < 1 or input_column > columns_number:
                    input_type = -2
                    raise ValueError
                input_type = -1
                empty_rows_in_column = game_entries[input_column - 1].index("NULL")
                game_entries[input_column - 1][empty_rows_in_column] = str(turn)
                valid_column = True
                final_state = draw_board(game_entries, columns_number, p1_symbol, p2_symbol, len(p1_symbol))
                game_over, p1_won, p2_won = check_game_status(game_entries, columns_number, rows_number, turn)
                turn = switch_turn(turn)

            except ValueError:
                if input_type == -1:
                    print("Column {} has no empty space.".format(input_column))
                elif input_type == -2:
                    print("Please enter a valid column number.")
                else:
                    print("Please enter a numeric value.")

    if game_over:
        print("Game over, It's a tie.")
    elif p1_won:
        print("Player 1 won.")
    else:
        print("Player 2 won.")

    return game_over, p1_won, p2_won, final_state


if __name__ == "__main__":
    configuration_file = "example.config"
    play(configuration_file)
