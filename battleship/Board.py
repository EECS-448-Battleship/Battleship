from .enum import BoardCellState


class Board:
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
            self.board.append([BoardCellState.Empty] * 9)

    def setUp(self, ship):
        """Places a ship on the board
        
        Places the ships on the board and signifies the ships place by using an "S".
        
        Args:
            ship: a ship object to be placed on the board.
        """

        for loc in ship.get_location_array():
            cLoc = convert_loc(loc)
            self.board[cLoc[0]][cLoc[1]] = BoardCellState.Ship

    def update(self, loc):
        """
        Updates the board when a player makes a move.  If the
        ship is hit, it will be signified on the board with a
        "X".  If the player shoots and there is no ship there it
        will be signified with a "*".
        
        Args:
            loc: the string location that is to be updated
        """
        hit = False

        cLoc = convert_loc(loc)
        current_value = self.board[cLoc[0]][cLoc[1]]

        if current_value == BoardCellState.Empty:
            self.board[cLoc[0]][cLoc[1]] = BoardCellState.Miss
        elif current_value == BoardCellState.Ship:
            self.board[cLoc[0]][cLoc[1]] = BoardCellState.Hit
            hit = True

        return hit

    def been_shot(self, loc):
        """ Returns if the spot has already been shot
        
        Args:
            loc: the string location that is to be updated
        """

        cLoc = convert_loc(loc)
        if cLoc != (99, 99):
            current_value = self.board[cLoc[0]][cLoc[1]]
            if current_value == BoardCellState.Empty or current_value == BoardCellState.Ship:
                return True

        return False
        
    def any_left(self):
        """check the win
        
        Returns:
            True: there is a ship left
            False: there is not a ship left
        """
        for row in self.board:
            for spot in row:
                if spot == BoardCellState.Ship:
                    return True
        return False

    def get_cell_status(self, loc_str):
        """get the state of the given cell

        Args:
            loc_str: the string location that is to be fetched
        """
        loc = convert_loc(loc_str)

        if loc == (99, 99):
            return BoardCellState.Unknown

        return self.board[loc[0]][loc[1]]

    def get_valid_placement_cells_for_ship(self, placed_row, placed_col, ship_length):
        """Get an array of valid coordinates where the second end of a ship of the given length might be placed.

        Args:
            placed_row: the row index of the first point
            placed_col: the col index of the first point
            ship_length: the number of cells long the ship is

        Returns:
            [(row, col)]
        """
        valid_coords = []
        ship_length_offset = ship_length - 1

        # Vertical upward
        if placed_row - ship_length_offset >= 0:
            coord = (placed_row - ship_length_offset, placed_col)
            intermediates = [coord]
            for row_idx in range(coord[0], placed_row):
                intermediates.append((row_idx, placed_col))

            if self.no_cell_as_ship(intermediates):
                valid_coords.append(coord)

        # Vertical downward
        if placed_row + ship_length_offset < 9:
            coord = (placed_row + ship_length_offset, placed_col)
            intermediates = [coord]
            for row_idx in range(placed_row, coord[0]):
                intermediates.append((row_idx, placed_col))

            if self.no_cell_as_ship(intermediates):
                valid_coords.append(coord)

        # Horizontal leftward
        if placed_col - ship_length_offset >= 0:
            coord = (placed_row, placed_col - ship_length_offset)
            intermediates = [coord]
            for col_idx in range(coord[1], placed_col):
                intermediates.append((placed_row, col_idx))

            if self.no_cell_as_ship(intermediates):
                valid_coords.append(coord)

        # Horizontal rightward
        if placed_col + ship_length_offset < 9:
            coord = (placed_row, placed_col + ship_length_offset)
            intermediates = [coord]
            for col_idx in range(placed_col, coord[1]):
                intermediates.append((placed_row, col_idx))

            if self.no_cell_as_ship(intermediates):
                valid_coords.append(coord)

        return valid_coords

    def cell_has_ship(self, loc_str):
        """returns true if the given cell has a ship, sunk or otherwise

        Args:
            loc_str: the string location that is to be checked
        """
        loc = convert_loc(loc_str)

        if loc == (99, 99):
            return False

        state = self.board[loc[0]][loc[1]]
        return state == BoardCellState.Ship or state == BoardCellState.Hit

    def no_cell_as_ship(self, coords):
        """Returns true if no cell for the given [(row, col), ...] coordinates contains a ship.
        """
        has_ship = False
        for coord in coords:
            has_ship = has_ship or self.cell_has_ship(coords_to_loc(coord[0], coord[1]))

        return not has_ship

    def cell_can_be_fired_upon(self, loc_str):
        """returns true if the given cell can be fired upon

        Args:
            loc_str: the string location that is to be checked
        """
        loc = convert_loc(loc_str)

        if loc == (99, 99):
            return False

        state = self.board[loc[0]][loc[1]]
        return state == BoardCellState.Ship or state == BoardCellState.Empty


def loc_string_is_valid(loc_str):
    """returns true if the given location string is valid

    Args:
        loc_str: the string location to be checked
    """

    return convert_loc(loc_str) != (99, 99)


def coords_to_loc(row, col):
    """Convert row, col coordinates to a location string "A1"
    Args:
        row: the row index
        col: the col index
    """
    letter = ''
    if col == 0:
        letter = 'A'
    elif col == 1:
        letter = 'B'
    elif col == 2:
        letter = 'C'
    elif col == 3:
        letter = 'D'
    elif col == 4:
        letter = 'E'
    elif col == 5:
        letter = 'F'
    elif col == 6:
        letter = 'G'
    elif col == 7:
        letter = 'H'
    elif col == 8:
        letter = 'I'

    return str(letter) + str(row + 1)


def convert_loc(loc):
    """ Coverts to array access tuple
    Converts the letters on the board to numbers that coorespond with the columns.
    
    Returns: 
        loc: if valid then it is tuple, if not then it is (99, 99)

    Args:
        loc: location string of form "A1" or "I8"
    """
    loc = (loc[0].upper(), loc[1])
    col = 0
    if loc[0] == "A":
        col = 0
    elif loc[0] == "B":
        col = 1
    elif loc[0] == "C":
        col = 2
    elif loc[0] == "D":
        col = 3
    elif loc[0] == "E":
        col = 4
    elif loc[0] == "F":
        col = 5
    elif loc[0] == "G":
        col = 6
    elif loc[0] == "H":
        col = 7
    elif loc[0] == "I":
        col = 8
    else:
        col = 99

    row = int(loc[1]) - 1
    if not ((row >= 0) and (row <= 8)):
        row = 99

    converted = (row, col)
    return converted
