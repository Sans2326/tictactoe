# --------- Global Variables -----------
print("\t\t\t\t******TIC TAC TOE GAME******\n\n")
# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
winner = None
p1 = input("Enter player name who goes for X:")
p2 = input("Enter player name who goes for O:")
current_player = p1

# ------------- Functions ---------------

def play_game():
    # Show the initial game board
    display_board()
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X":
        print(p1 + " won.")
    elif winner =="O":
        print(p2 + " won.")
    elif winner is None:
        print("Tie.")

# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position]=="-":
            valid = True
        else:
            print("Already filled. Go again.")

    # Put the game piece on the board
    if player == p1:
        board[position] = "X"
    else:
        board[position] = "O"

    # Show the game board
    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going

    row_1 = board[0]==board[1]==board[2]!="-"
    row_2 = board[3]==board[4]==board[5]!="-"
    row_3 = board[6]==board[7]==board[8]!="-"
    # If any row does is completely filled it means we have a winner
    if row_1 or row_2 or row_3:
        game_still_going = False  # game should be stopped now
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None

    # Check the columns for a win
def check_columns():
    global game_still_going

    column_1 = board[0]==board[3]==board[6]!="-"
    column_2 = board[1]==board[4]==board[7]!="-"
    column_3 = board[2]==board[5]==board[8]!="-"
    # If any column does is completely filled it means we have a winner
    if column_1 or column_2 or column_3:
        game_still_going = False  # game should be stopped

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    else:
        return None


def check_diagonals():
    global game_still_going

    diagonal_1 = board[0]==board[4]==board[8]!="-"
    diagonal_2 = board[2]==board[4]==board[6]!="-"

    # If any diagonal does is completely filled it means we have a winner
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    else:
        return None


def check_for_tie():

    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player

    if current_player==p1:
        current_player = p2

    elif current_player==p2:
        current_player = p1


# Play a game of tic tac toe
play_game()