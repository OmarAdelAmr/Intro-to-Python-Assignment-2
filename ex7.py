from ex6 import play


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

    score_board = "\nSCORES OF ALL ROUNDS:\n----------------------\n\n"

    for counter in range(rounds_number):
        game_over, p1_won, p2_won, final_state = play(file_name)

        score_board += "Round {} score:\n\n".format(counter + 1)
        if p1_won:
            p1_counter += 1
            score_board += "Player 1 won tis round.\n"
        elif p2_won:
            p2_counter += 1
            score_board += "Player 2 won tis round.\n"
        else:
            score_board += "It's a tie.\n"

        score_board += final_state + "\n-----------------------------------\n\n"

    score_board += "OVER ALL TOURNAMENT SCORE:\n\n"
    if p1_counter > p2_counter:
        score_board += "PLAYER 1 IS THE WINNER OF THIS TOURNAMENT."
    elif p2_counter > p1_counter:
        score_board += "PLAYER 2 IS THE WINNER OF THIS TOURNAMENT."
    else:
        score_board += "IT'S A TIE, BOTH PLAYERS WON THE SAME NUMBER OF GAMES."

    print(score_board)
    output = open("Results.txt", "w")
    output.write(score_board)
    output.close()


# TODO: Ask where the output file should be
if __name__ == "__main__":
    config_file = "example.config"
    rounds(config_file)
