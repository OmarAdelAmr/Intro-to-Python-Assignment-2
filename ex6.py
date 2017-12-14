from ex5 import read_input_file
import numpy as np


def switch_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


def draw_board(rows, columns, p1_symbol, p2_symbol, game_entries):
    vertical_bars = rows * len(p1_symbol) + (rows - 1)
    symbol_size = len(p1_symbol)

    game_entries = [list(x) for x in game_entries]
    game_entries = np.flip(np.transpose(game_entries), 0)
    # print(game_entries[0])

    # xx = [game_entries.x for x in game_entries[4] if x != "NULL"]
    xxx = game_entries[4][game_entries[4] != "NULL"]
    xxx = np.nonzero(game_entries[4] != "NULL")
    print(xxx[0][0])
    # print("-->", xxx)

    board = ""

    for row_counter in range(rows):
        non_empty_values = np.nonzero(game_entries[row_counter] != "NULL")
        non_empty_indices = np.nonzero(game_entries[row_counter] != "NULL")
        print(non_empty_indices)
        current_row_counter = 0

        for counter in range(symbol_size):
            line = "|," * (columns + 1)
            line = line[:len(line) - 1]
            current_row_counter += 1

            # if game_entries[row_counter][column_counter] != "NULL":

            # print(game_entries[row_counter][column_counter])

        line = "|," * (columns + 1)
        line = line[:len(line) - 1]
        if current_row_counter == symbol_size:
            line = line.replace(",", "-" * symbol_size)
        else:
            line = line.replace(",", " " * symbol_size)

        board += "\n" + line

    board += "\n" + "-" * (symbol_size * columns + (columns + 1))

    return board


def insert_bars(l):
    result = ["|"] * (len(l) * 2)
    result[0::2] = l
    result = "|" + "".join(str(x) for x in result)
    return result


def visualize_board(board):
    for line in board:
        print(line)


def draw_board2(column, row, symbol, board, height):
    symbol_size = len(symbol)

    start_index = height - (row * symbol_size + row)

    change_rows = range(start_index, start_index + symbol_size)

    for x in change_rows:
        r = board[height - x]
        temp_symbol = symbol[x % symbol_size]
        r = r.split("|")
        r = r[1:len(r) - 1]
        r[symbol_size] = temp_symbol
        r = insert_bars(r)
        r = "".join(str(x) for x in r)
        board[height - x] = r

    visualize_board(board)

    return board
    print("TODO")


def play(config_file):
    board, p1_symbol, p2_symbol, columns_number, rows_number = read_input_file(config_file)
    # print(board)
    game_over, p1_won, p2_won = [False, False, False]
    turn = 1

    game_entries = [["NULL" for x in range(rows_number)] for y in range(columns_number)]  # array list of each column

    while not (game_over and p1_won and p2_won):
        valid_column = False
        while not valid_column:
            try:
                empty_rows_in_column = -1
                input_column = int(input("Player's {} turn: ".format(turn)))
                if input_column < 1 or input_column > columns_number:
                    empty_rows_in_column = -2
                    raise ValueError
                empty_rows_in_column = game_entries[input_column - 1].index("NULL")
                game_entries[input_column - 1][empty_rows_in_column] = turn
                turn = switch_turn(turn)
                # print(game_entries)
                # print(input_column - 1)
                # print(empty_rows_in_column)
                # print("row", empty_rows_in_column)
                board = draw_board2(input_column - 1, empty_rows_in_column, p1_symbol, board, columns_number)
                # draw_board(rows_number, columns_number, p1_symbol, p2_symbol, game_entries)
            except ValueError:
                if empty_rows_in_column == -1:
                    print("Column {} has no empty space.".format(input_column))
                elif empty_rows_in_column == -2:
                    print("Please enter a valid column number.")
                else:
                    print("Please enter a numeric value.")

        print("outside inner loop")

    # print(board)


if __name__ == "__main__":
    file_name = "example.config"
    play(file_name)
