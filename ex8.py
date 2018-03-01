#!/usr/bin/env python3
"""ex8.py
Author: Omar Amr
Matr.Nr.: K11776960
Exercise 8
"""

from ex5 import read_input_file
from ex6 import switch_turn
from ex6 import check_game_status
from ex6 import draw_board
from ex7 import rounds


def play_tournament_bonus(config_file):
    valid = False
    rounds_number = ""
    while not valid:
        try:
            rounds_number = int(input("Please enter how many rounds you would like to play: "))
            if rounds_number < 1:
                raise ValueError
            valid = True
        except ValueError:
            print("Please enter a number greater than 0.")

    p1_counter = 0
    p2_counter = 0

    score_board = "-*-*-*-*-*-*-*-*-*-*-*-*-\n"
    score_board += "| SCORES OF ALL ROUNDS  |\n"
    score_board += "-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"

    for counter in range(rounds_number):
        game_over, p1_won, p2_won, final_state = play_bonus(config_file)

        score_board += "Round {} score:\n\n".format(counter + 1)
        if p1_won:
            p1_counter += 1
            score_board += "Player 1 won this round.\n"
        elif p2_won:
            p2_counter += 1
            score_board += "Player 2 won this round.\n"
        else:
            score_board += "It's a tie.\n"

        score_board += final_state + "\n\n-----------------------------------\n\n"

    score_board += "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n"
    score_board += "| OVERALL TOURNAMENT SCORE |\n"
    score_board += "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"
    if p1_counter > p2_counter:
        score_board += "PLAYER 1 IS THE WINNER OF THIS TOURNAMENT."
    elif p2_counter > p1_counter:
        score_board += "PLAYER 2 IS THE WINNER OF THIS TOURNAMENT."
    else:
        score_board += "IT'S A TIE, BOTH PLAYERS WON THE SAME NUMBER OF GAMES."

    print(score_board)
    output = open("Results Bonus.txt", "w")
    output.write(score_board)
    output.close()


def play_bonus(config_file):
    board, p1_symbol, p2_symbol, columns_number, rows_number = read_input_file(config_file)
    game_over, p1_won, p2_won = [False, False, False]
    turn = 1
    final_state = ""

    game_entries = [["NULL" for x in range(rows_number)] for y in range(columns_number)]  # array list of each column

    while not (game_over or p1_won or p2_won):
        valid_column = False
        while not valid_column:
            try:
                input_type = 0
                print("Player's {} turn: ".format(turn))
                user_input = input(
                    "Please enter column number followed by a space then push or pull. Example: 1 push or 1 pull\n>>")
                user_input = user_input.split()

                try:
                    input_column = int(user_input[0])
                    operation = user_input[1]
                except IndexError:
                    print("\nInput is not valid.\n")
                    break

                if input_column < 1 or input_column > columns_number:
                    input_type = -2
                    raise ValueError

                if operation == "push":
                    input_type = -1
                    empty_rows_in_column = game_entries[input_column - 1].index("NULL")
                    game_entries[input_column - 1][empty_rows_in_column] = str(turn)
                    valid_column = True
                    final_state = draw_board(game_entries, columns_number, p1_symbol, p2_symbol, len(p1_symbol))
                    game_over, p1_won, p2_won = check_game_status(game_entries, columns_number, rows_number, turn)
                    turn = switch_turn(turn)
                elif operation == "pull":
                    empty_rows_in_column = game_entries[input_column - 1]
                    if empty_rows_in_column[0] != str(turn):
                        input_type = -4
                        raise ValueError
                    else:
                        temp_column = game_entries[input_column - 1]
                        temp_column.append("NULL")
                        del temp_column[0]
                        game_entries[input_column - 1] = temp_column
                        valid_column = True
                        final_state = draw_board(game_entries, columns_number, p1_symbol, p2_symbol, len(p1_symbol))
                        game_over, p1_won, p2_won = check_game_status(game_entries, columns_number, rows_number, turn)
                        # TODO: following if condition not working properly
                        if any(item is False for item in [game_over, p1_won, p2_won]):
                            other_check = switch_turn(turn)
                            game_over, p1_won, p2_won = check_game_status(game_entries, columns_number, rows_number,
                                                                          other_check)
                        turn = switch_turn(turn)
                else:
                    print("\nInput is not valid.\n")
                    break

            except ValueError:
                if input_type == -1:
                    print("\nColumn {} has no empty space.\n".format(input_column))
                elif input_type == -2:
                    print("\nPlease enter a valid column number between 1 and {}.\n".format(columns_number))
                elif input_type == -4:
                    print("\nPlayer {} cannot pull from column {}.\n".format(turn, input_column))
                else:
                    print("\nInput is not valid.\n")

    if game_over:
        print("Game over, It's a tie.")
    elif p1_won:
        print("Player 1 won.")
    else:
        print("Player 2 won.")

    return game_over, p1_won, p2_won, final_state


if __name__ == "__main__":
    configuration_file = "example.config"
    accepted_input = False
    while not accepted_input:
        selected_mode = input("Press 1 for Normal Mode or 2 for Pop Out Mode: ")
        if selected_mode == "1":
            accepted_input = True
            rounds(configuration_file)
        elif selected_mode == "2":
            accepted_input = True
            play_tournament_bonus(configuration_file)
        else:
            print("Not a valid input.")
