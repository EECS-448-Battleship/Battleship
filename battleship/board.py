from .Ship import Ship

class board:

    """ The class to abstract the board

    Attributes:
        board: the array that will hold the data. O for open. * for miss. S for ship. X for hit ship.
    """

    # Creates a 9x9 board of O's.

    def __init__(self):
        """ Inits the board


        """

        self.board = []
        for _ in range(0, 9):
            self.board.append(["O"] * 9)



    def setUp(self, ship):
        """Places a ship on the board
        
        Places the ships on the board and signifies the ships place by using an "S".
        
        Args:
            ship: a ship object to be placed on the board.
        """

        for loc in ship.get_location_array():
            cLoc = convert_loc(loc)
            self.board[cLoc[0]][cLoc[1]] = "S"

 


    def update(self, loc):
        """
        Updates the board when a player makes a move.  If the
        ship is hit, it will be signified on the board with a
        "X".  If the player shoots and there is no ship there it
        will be signified with a "*".
        
        Args:
            loc: the string location that is to be updated
        """
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

    def been_shot(self, loc):
        """ Returns if the spot has already been shot
        
        Args:
            loc: the string location that is to be updated
        """

        cLoc = convert_loc(loc)
        if cLoc != (99,99):
            current_value = self.board[cLoc[0]][cLoc[1]]
            if current_value == "O" or current_value == "S":
                return True
        return False
        


def convert_loc(loc):
    """ Coverts to arry access tuple
    Converts the letters on the board to numbers that coorespond with the columns.
    
    Returns: 
        loc: if valid then it is tuple, if not then it is (99, 99)

    Args:
        loc: location string of form "A1" or "I8"
    """
    loc = (loc[0].upper(), loc[1])
    col = 0
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
    else:
        col = 99

    row = int(loc[1]) -1
    if not((row >= 0) and (row<=8)):
        row == 99
    coverted = (row,col)

    return coverted
