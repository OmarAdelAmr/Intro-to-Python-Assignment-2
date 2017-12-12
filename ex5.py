def get_content_between_quotations(input_string):
    input_string = str(input_string)
    start = input_string.index('"') + 1
    end = input_string[start:].index('"') + start
    result = input_string[start:end]

    return result


def validate_players_symbol(symbol1, symbol2):
    symbol1_rows = len(symbol1)
    symbol2_rows = len(symbol2)

    valid = True
    if symbol1_rows != symbol2_rows:
        valid = False

    if symbol1_rows < 1 or symbol1_rows > 4:
        valid = False

    for x in symbol1 + symbol2:
        if len(x) != symbol1_rows:
            valid = False

    if not valid:
        print("Players' symbols are not valid")
        return


def draw_board(rows, columns, symbol_size):
    vertical_bars = rows * symbol_size + (rows - 1)

    board = ""

    row_separation_counter = 0
    for counter in range(vertical_bars):

        line = "|," * (columns + 1)
        line = line[:len(line) - 1]
        if row_separation_counter == symbol_size:
            line = line.replace(",", "-" * symbol_size)
            row_separation_counter = 0
        else:
            line = line.replace(",", " " * symbol_size)
            row_separation_counter += 1
        board += "\n" + line

    board += "\n" + "-" * (symbol_size * columns + (columns + 1))

    return board


def read_input_file(file):
    file_content = open(file, 'r').read()
    file_content = file_content.splitlines()
    columns = 0
    rows = 0
    p1_symbol = ""
    p2_symbol = ""

    for x in file_content:
        if x.startswith("width"):
            columns = int(x.split("=")[1])

        elif x.startswith("height"):
            rows = int(x.split("=")[1])

        elif x.startswith("player1_symbol"):
            p1_symbol = x.split("=")[1].split(",")
            p1_symbol = [get_content_between_quotations(item) for item in p1_symbol]

        elif x.startswith("player2_symbol"):
            p2_symbol = x.split("=")[1].split(",")
            p2_symbol = [get_content_between_quotations(item) for item in p2_symbol]

    validate_players_symbol(p1_symbol, p2_symbol)
    board = draw_board(rows, columns, len(p1_symbol))

    return board, p1_symbol, p2_symbol, columns, rows


if __name__ == "__main__":
    file_name = "example.config"
    playing_board = read_input_file(file_name)
    print(playing_board[0])
