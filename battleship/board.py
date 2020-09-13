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

        for loc in ship.get_location_array():
            cLoc = convert_loc(loc)
            self.board[cLoc[0]][cLoc[1]] = "S"           

    #update function
    def update(self, loc):
        
        success = True

        cLoc = convert_loc(loc)
        current_value = self.board[cLoc[0]][cLoc[1]]
        
        if current_value == "O":
            self.board[cLoc[0]][cLoc[1]] = "*"
        elif current_value == "S":
            self.board[cLoc[0]][cLoc[1]] = "X"
        else:
            success = False
        
        return success



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

    row = int(loc[1]) -1

    coverted = (row,col)

    return coverted