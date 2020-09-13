from class_ship import Ship

class board:

    """


    """

    #creating 9 by 9 board of O's
    def __init__(self):
        self.board = []
        for i in range(0, 9):
            self.board.append(["O"] * 9)

    # # #printing the board with spaces in between
    # def print_board(board):
    #     for row in board:



    #setup function that places the ships and places them on the board
    def setUp(self, ship):
        """
        Takes a ship and places it on the board


        """

        
        for ship in range(0, 9):
            if (set_ships(ship) == true):
                board.append(["S"])

    #update function
    def update(self, loc):
        for ship in range(0, 9):
            if (hit(ship) == true):
                board.append(["X"])
            else:
                board.append(["*"])


def convert_loc(loc):
    """

    """
    if (loc[0] == "A"):
        col = 0
    elif (loc[0] == "B"):
        col = 1
    elif (loc[0] == "C"):
        col = 2
    elif (loc[0] == "D"):
        col = 3
    elif (loc[0] == "E"):
        col = 4
    elif (loc[0] == "F"):
        col = 5
    elif (loc[0] == "G"):
        col = 6
    elif (loc[0] == "H"):
        col = 7
    elif (loc[0] == "I"):
        col = 8
    

    x = loc[0]

    y = int(loc[1]) -1

    coverted = (x,y)

    return coverted