def create_board():
    return [[" "," "," "],
            [" "," "," "],
            [" "," "," "]] # Empty whitespace means it's empty

def display_board(board):
    for row in board:
        print("|".join(row))
        print("─────")

def get_player_move(player):
    while True:
        try:
            rowMove = int(input("Row (1-3): ")) - 1
            columnMove = int(input("Column (1-3): ")) - 1
            if rowMove in range(0, 3) and columnMove in range(0, 3):
                return rowMove, columnMove
            print("Invalid move. Choose a row and column from 1 to 3.")
        except (TypeError, ValueError):
            print("Invalid move. Enter numbers from 1 to 3.")

def is_valid_move(board, row, column):
    # check if its within expected range
    if row in range(0,3) and column in range(0,3): # not inclusive of 3
        if board[row][column] == " ": ## If it's empty, return True
            return True
        else:
            return False

def make_move(board, row, column, player): # row horizontal, column vertical - select row first
    try:
        if player == 0: # Player 0 = X
            board[row][column] = "X"
        elif player == 1: # Player 1 = O
            board[row][column] = "O"
    except Exception as e:
        print(f"Error making move: {e}")

def check_rows(board, player):
    indicator = ""
    # check first row
    if player == 0: # X
        indicator = "X"
    elif player == 1: # O
        indicator = "O"

    completed = False
    for i in range(0,3):
            if board[i][0] == indicator and board[i][1] == indicator and board[i][2] == indicator:
                completed = True

    if completed == True:
        return True
    elif completed == False:
        return False

def check_columns(board, player):
    indicator = ""
    # check first row
    if player == 0: # X
        indicator = "X"
    elif player == 1: # O
        indicator = "O"

    completed = False
    for i in range(0,3):
        if board[0][i] == indicator and board[1][i] == indicator and board[2][i] == indicator:
            completed = True

    if completed == True:
        return True
    elif completed == False:
        return False

def check_diagonals(board, player):
    indicator = ""
    # check first row
    if player == 0: # X
        indicator = "X"
    elif player == 1: # O
        indicator == "O"

    if (board[0][0] == indicator and
        board[1][1] == indicator and
        board[2][2] == indicator):
        return True

    if (board[0][2] == indicator and
        board[1][1] == indicator and
        board[2][0] == indicator):
        return True

    return False

def check_winner(board, player):
    return (check_rows(board, player) or
            check_columns(board, player) or
            check_diagonals(board, player))

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def switch_player(player):
    if player == 0: # X
        return 1 # O
    else:
        return 0 # X

def get_indicator(player):
    indicator = ""
    if player == 0: # X
        return "X"
    elif player == 1: # O
        return "O"

def play_game():
    board = create_board()
    player = 0 # 0 = X

    while True:
        display_board(board)
        row, column = get_player_move(player)
        if is_valid_move(board, row, column):
            make_move(board, row, column, player)
        else:
            print("That square is already taken.")
            continue

        display_board(board)

        if check_winner(board, player):
            print(f"Player {get_indicator(player)} has won!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        player = switch_player(player)

def main():
    # myboard = create_board()
    # current_player = 0 # 0 = X, 1 = O
    # print(display_board(myboard))
    # # print(is_valid_move(myboard, 2,2))
    # # make_move(myboard, 2,2, current_player)
    # # print(display_board(myboard))
    # # print(is_valid_move(myboard, 2,2))
    # print(f"Check rows:{check_rows(myboard, current_player)}")
    # print(f"Check columns:{check_columns(myboard, current_player)}")
    # print(check_diagonals(myboard, current_player))
    play_game()

if __name__ == "__main__":
    main()