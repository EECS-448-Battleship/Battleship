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

#setup function that places the ships and places them on the board
def setUp():
    for i in range(0, 9)
        if (set_ships(i) == true)
            board.append(["S"])

#update function
def update():
    for i in range(0, 9):
        if (hit(i) == true)
            board.append(["X"])
