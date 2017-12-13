from ex5 import read_input_file


def switch_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


def draw_board(rows, columns, p1_symbol, p2_symbol, game_entries):
    vertical_bars = rows * len(p1_symbol) + (rows - 1)
    print(game_entries)
    board = ""

    # row_separation_counter = 0
    # for counter in range(vertical_bars):
    #
    #     line = "|," * (columns + 1)
    #     line = line[:len(line) - 1]
    #     if row_separation_counter == symbol_size:
    #         line = line.replace(",", "-" * symbol_size)
    #         row_separation_counter = 0
    #     else:
    #         line = line.replace(",", " " * symbol_size)
    #         row_separation_counter += 1
    #     board += "\n" + line
    #
    # board += "\n" + "-" * (symbol_size * columns + (columns + 1))
    #
    # return board


def play(config_file):
    board_configuration = read_input_file(config_file)
    board = board_configuration[0]
    p1_symbol = board_configuration[1]
    p2_symbol = board_configuration[2]
    columns_number = board_configuration[3]
    rows_number = board_configuration[4]

    print(p1_symbol)

    game_over = False
    p1_won = False
    p2_won = False
    turn = 1

    game_entries = [["NULL" for x in range(rows_number)] for y in range(columns_number)]  # array list of each column

    print(game_entries[0])

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
                draw_board(rows_number, columns_number, p1_symbol, p2_symbol, game_entries)
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
