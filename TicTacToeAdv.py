import sys

matrix=3
board=[]
game_is_on=True
place=0
winner = None
curr_player="X"
continueFlag=0

def reset_game():
    global matrix
    global board
    global game_is_on
    global place
    global winner
    global curr_player
    matrix = 3
    board = []
    game_is_on = True
    place = 0
    winner = None
    curr_player = "X"
    return


def display_board():
    global matrix
    boardpos = 0
    for i in range(int(matrix)):
        for j in range(int(matrix)):
            sys.stdout.write(board[boardpos])
            sys.stdout.write("|")
            boardpos = boardpos + 1
        sys.stdout.write("\b")
        sys.stdout.write("\n")
        sys.stdout.flush()


def handel_turn(player):
    global matrix
    m=(int(matrix)*int(matrix))
    print(player + "   Turn now:")
    pos=input(f"Choose a positionfrom 1-{m}:")
    curboard=[]
    v=1
    for i in range((int(matrix))):
        for j in range((int(matrix))):
            curboard.append(v)
            v=v+1
    valid = False
    while not valid:
        while int(pos) not in curboard:
            pos = input(f"Invalid input. Choose a positionfrom 1-{m}:")
        position=int(pos)-1
        if board[position] == '-':
            valid= True
        else:
            print("Position is already used")
            break
    board[position]=player
    display_board()


def start_up():
    global curr_player
    global matrix
    global continueFlag
    matrix=input("Which matrix you want to play?")
    if matrix.isdigit():
        if (int(matrix)) < 3:
            print("Not a valid version")
            print("Matrix set to default: 3")
            matrix=3
        print("Setting up your board")
    else:
        print("Not a suitable matrix for Tic Tac Toe")
        print("Setting default matrix to: 3")
        matrix=3
        print("Setting up your board")
    for i in range(int(matrix)):
        for j in range(int(matrix)):
            board.append("-")
    start_player=input("Who should start? X or O")
    while start_player not in ['o','O','x','X']:
        print("Not a valid player. Choose X or O:")
        start_player = input("Who should start?")
    curr_player=start_player.upper()
    # print("Flag:", continueFlag)
    if continueFlag==1:
        play_game()
    return

def play_game():
    global winner
    global game_is_on
    global continueFlag
    display_board()
    while game_is_on:
        handel_turn(curr_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner, "WON!!")
    elif winner ==None:
        print("TIE!!")
    userDec=input("Do you want another game? Y/N")
    if userDec == 'Y' or userDec=='y':
        print("Lets Start Again:::")
        continueFlag = 1
        reset_game()
        start_up()
    else:
        continueFlag=0
        print("Bye!!")


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_rows_advanced()
    col_winner = check_cols_advanced()
    diag_winner = check_diags_advanced()
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


def check_rows_advanced():
    global matrix
    global game_is_on
    global board
    matrixVal = int(matrix)
    rowChk = []
    pos = 0
    for i in range(matrixVal):
        rowVal = []
        for j in range(matrixVal):
            rowVal.append(board[pos])
            pos=pos+1
        # res = all(ele == rowVal[0] for ele in rowVal)
        ele=board[pos-1]
        chk=True
        for item in rowVal:
            if ele!=item or item=="-":
                chk=False
                break
            else:
                chk=True
        if chk:
            game_is_on = False
            rowChk.append("True")
            return board[pos - 1]
        else:
            rowChk.append("False")
    return


def check_cols_advanced():
    global matrix
    global game_is_on
    global board
    colChkBoard=transpose(board)
    matrixVal = int(matrix)
    colChk = []
    pos = 0
    for i in range(matrixVal):
        colVal = []
        for j in range(matrixVal):
            colVal.append(colChkBoard[pos])
            pos = pos + 1
        ele = colChkBoard[pos - 1]
        chk = True
        for item in colVal:
            if ele != item or item == "-":
                chk = False
                break
            else:
                chk = True
        if chk:
            game_is_on = False
            colChk.append("True")
            return colChkBoard[pos - 1]
        else:
            colChk.append("False")
    return

def transpose(b):
    global matrix
    m=int(matrix)
    transposedBoard=[]
    for i in range((int(matrix))):
        for j in range((int(matrix))):
            transposedBoard.append(b[((j * m) + i)-1])

    return transposedBoard


def check_diags_advanced():
    global matrix
    global game_is_on
    global board
    diagChkBoard=mirror(board)
    d1=diagChecker(board)
    d2=diagChecker(diagChkBoard)
    if d1=="X" or d1=="O":
        return d1
    elif d2=="X" or d2=="O":
        return d2
    return

def diagChecker(b):
    global matrix
    global game_is_on
    matrixVal = int(matrix)
    pos = 0
    diag = []
    diagChk = []
    for i in range(matrixVal):
        for j in range(matrixVal):
            if i == j:
                diag.append(b[pos])
            pos = pos + 1
    ele = diag[2]
    for item in diag:
        if ele != item or item == "-":
            chk = False
            break
        else:
            chk = True
    if chk:
        game_is_on = False
        diagChk.append("True")
        return diag[0]
    else:
        diagChk.append("False")
    return


def mirror(b):
    global matrix
    mirroredBoard=[]
    m=int(matrix)
    n = int(matrix)
    for i in range((int(matrix))):
        m = n * (i + 1)
        for j in range((int(matrix))):
            mirroredBoard.append(b[m-1])
            m=m-1
    return mirroredBoard


def flip_player():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    return

#handle game flow
start_up()
play_game()
