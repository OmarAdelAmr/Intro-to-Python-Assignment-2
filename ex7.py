#!/usr/bin/env python3
"""ex7.py
Author: Omar Amr
Matr.Nr.: K11776960
Exercise 7
"""

from ex6 import play


# This function takes the number of rounds to be player as input from the user. Then it calls the the plat function
# from ex6. Each round is accumulated to a string and eventually this string is written to "Results.txt" file.
def rounds(file_name):
    valid = False
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
        game_over, p1_won, p2_won, final_state = play(file_name)

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

    # Write results to text file.
    print(score_board)
    output = open("Results.txt", "w")
    output.write(score_board)
    output.close()


# Main function
if __name__ == "__main__":
    config_file = "example.config"
    rounds(config_file)
