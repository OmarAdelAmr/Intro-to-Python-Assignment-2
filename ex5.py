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

    return valid


def draw_board(rows, columns, symbol_size):
    line = " " * columns * symbol_size + "\n"
    line = line * rows * symbol_size
    board = line.split("\n")
    board = [x for x in board if x != ""]

    return board


def visualize_board(board, columns, symbol_size):
    result = ""
    separator_counter = 0
    for line in board:
        result += "|" + '|'.join(line[i:i + symbol_size] for i in range(0, len(line) + 1, symbol_size)) + "\n"
        separator_counter += 1
        if separator_counter == symbol_size:
            separator = "|" * (columns + 1)
            separator = ('-' * symbol_size).join(separator[i:i + 1] for i in range(0, len(separator), 1)) + "\n"
            result += separator
            separator_counter = 0
    result = result[:(result[:result.rfind('\n')]).rfind('\n')]  # remove last 2 lines
    result += "\n" + "-" * (columns * symbol_size + columns + 1)

    print(result)


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

    if not validate_players_symbol(p1_symbol, p2_symbol):
        print("Players' symbols are not valid")
        return

    board = draw_board(rows, columns, len(p1_symbol))
    visualize_board(board, columns, len(p1_symbol))

    return board, p1_symbol, p2_symbol, columns, rows


if __name__ == "__main__":
    file_name = "example.config"
    playing_board = read_input_file(file_name)
