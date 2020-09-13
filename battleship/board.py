from class_ship import Ship

class board:

    """
    """

    # Creates a 9x9 board of O's.

    def __init__(self):
        self.board = []
        for i in range(0, 9):
            self.board.append(["O"] * 9)

    # Places the ships on the board and signifies the ships place
    # by using an "S".

    def setUp(self, ship):
        """
        Takes a ship and places it on the board
        """

        for loc in ship.get_location_array():
            cLoc = convert_loc(loc)
            self.board[cLoc[0]][cLoc[1]] = "S"

    # Updates the board when a player makes a move.  If the
    # ship is hit, it will be signified on the board with a
    # "X".  If the player shoots and there is no ship there it
    # will be signified with a "*".


    def update(self, loc):

        success = True

        cLoc = convert_loc(loc)
        current_value = self.board[cLoc[0]][cLoc[1]]

        if current_value == "0":
            self.board[cLoc[0]][cLoc[1]] = "*"
        elif current_value == "S":
            self.board[cLoc[0]][cLoc[1]] = "X"
        else:
            success = False

        return success

# Converts the letters on the board to numbers that coorespond
# with the columns.

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
