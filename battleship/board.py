from class_ship import Ship

class board:

    #creating 9 by 9 board of O's
    def __init__(self):
        self.board = []
        for i in range(0, 9):
            self.board.append(["O"] * 9)

    # # #printing the board with spaces in between
    # def print_board(board):
    #     for row in board:



    #setup function that places the ships and places them on the board
    def setUp():
        for ship in range(0, 9):
            if (set_ships(ship) == true):
                board.append(["S"])

    #update function
    def update():
        for ship in range(0, 9):
            if (hit(ship) == true):
                board.append(["X"])
            else
                board.append(["*"])
