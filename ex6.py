from ex5 import read_input_file


def visualize_board():  # TODO
    print("TODO")


def play(config_file):
    board_configuration = read_input_file(config_file)
    board = board_configuration[0]
    p1_symbol = board_configuration[1]
    p2_symbol = board_configuration[2]
    columns_number = board_configuration[3]
    rows_number = board_configuration[4]

    print(board)

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
                print(input_column)  # check index inside boundaries
                empty_rows_in_column = game_entries[input_column - 1].index("NULL")
                game_entries[input_column - 1][empty_rows_in_column] = turn
            except ValueError:
                if empty_rows_in_column == -1:
                    print("Column {} has no empty space.")
                else:
                    print("Please enter a numeric value.")

        print("outside inner loop")

    # print(board)


if __name__ == "__main__":
    file_name = "example.config"
    play(file_name)
