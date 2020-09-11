class board:

#creating 9 by 9 board of O's
def board():
    board = []
    for i in range(0, 9):
        board.append(["O"] * 9)

#printing the board with spaces in between
def print_board(board):
    for i in board:
        print " ".join(i)

#assigning the ship to the row/col coord that P1 inputs
P1ship_row = int(raw_input("Ship Row: "))
P1ship_col = int(raw_input("Ship Column: "))

#assigning the ship to the row/col coord that P1 inputs
P2ship_row = int(raw_input("Ship Row: "))
P2ship_col = int(raw_input("Ship Column: "))

#takes in the users guess
P1guess_row = int(raw_input("Guess Row: "))
P1guess_col = int(raw_input("Guess Column: "))

#takes in the users guess
P2guess_row = int(raw_input("Guess Row: "))
P2guess_col = int(raw_input("Guess Column: "))

#printing an X where the user guessed if the guess is correct
if (P1guess_row == P2ship_row && P1guess_col == P2ship_col)
    print "Ship has been hit! (this will be denoted by an X)"
    board[P1guess_row][P1guess_col] == "X"
    print_board(board)
elif (P2guess_row == P1ship_row && P2guess_col == P1ship_col)
    print "Ship has been hit! (this will be denoted by an X)"
    board[P2guess_row][P2guess_col] == "X"
    print_board(board)

#printing an * where the user guessed if the guess was a miss
else
    if P1guess_row or P2guess_row > range(9) or P1guess_col or P2guess_col > range(9)
        print "Guess is not in range"

    elif board[P1guess_row][P1guess_col] or board[P2guess_row][P2guess_col] == "X" or board[P1guess_row][P1guess_col] or board[P2guess_row][P2guess_col] == "*"
        print "You guessed that one already"

    else
    print "You missed! (this will be denoted by an *)"
    board [guess_row][guess_col] == "*"
    print_board(board)
