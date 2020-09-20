import sys

###Global Variables
board=["-","-","-","-","-","-","-","-","-"]
game_is_on =True
winner = None
curr_player="X"

def display_board():
    # print(board[0] + "|" + board[1] + "|" + board[2])
    # print(board[3] + "|" + board[4] + "|" + board[5])
    # print(board[6] + "|" + board[7] + "|" + board[8])
    # for i in range(3):
    #     for j in range(3):
    #         print(board[i], end="|")
    #     print()
    boardpos=0
    for i in range(3):
        for j in range(3):
            sys.stdout.write(board[boardpos])
            sys.stdout.write("|")
            boardpos=boardpos+1
        sys.stdout.write("\b")
        sys.stdout.write("\n")
        sys.stdout.flush()

def handel_turn(player):
    print(player + "   Turn now:")
    pos=input("Choose a positionfrom 1-9:")
    valid = False
    while not valid:
        while pos not in ['1','2','3','4','5','6','7','8','9']:
            pos = input("Invalid input. Choose a positionfrom 1-9:")
        position=int(pos)-1
        if board[position] == '-':
            valid= True
        else:
            print("Position is already used")
    board[position]=player
    display_board()


def start_up():
    global curr_player
    setup=input("which matrix you want to play?")
    start_player=input("Who should start?")
    while start_player not in ['o','O','x','X']:
        print("Not a valid player. Choose X or O:")
        start_player = input("Who should start?")
    curr_player=start_player.upper()
    return

def play_game():
    global winner
    global game_is_on
    display_board()
    while game_is_on:
        handel_turn(curr_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner, "WON!!")
    elif winner ==None:
        print("TIE!!")


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_rows()
    col_winner = check_cols()
    diag_winner = check_diags()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return


def check_if_tie():
    global game_is_on
    if "-" not in board:
        game_is_on= False
    return


def check_rows():
    global game_is_on
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_is_on = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_rows_advanced():
    global game_is_on
    matrixVal=4
    rowval=[]
    rowpos=[]
    pos=0
    for i in matrixVal:
        for j in matrixVal:
            rowval.append()

    # row1 = board[0] == board[1] == board[2] != "-"
    # row2 = board[3] == board[4] == board[5] != "-"
    # row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_is_on = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_cols():
    global game_is_on
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_is_on = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def check_diags():
    global game_is_on
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[6] == board[4] == board[2] != "-"
    if diag1 or diag2:
        game_is_on = False
    if diag1:
        return board[0]
    elif diag2:
        return board[6]
    return


def flip_player():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    return

#handel game flow
start_up()
play_game()