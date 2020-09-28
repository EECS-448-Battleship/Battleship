import os
from .Ship import Ship
from .board import board, convert_loc, loc_string_is_valid
from .enum import BoardCellState


class Player:
    def __init__(self, name):
        self.ships = []
        self.board = board()
        self.name = name
        self.other_player = None
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def set_other_player(self, player2):
        self.other_player = player2

    def is_floating(self):
        for ship in self.ships:
            for spot in ship.is_hit_array:
                if not spot:
                    return True
        return False

    def fire(self):
        """ Takes the players turn to fire

        Returns:
            True: has hit a ship
            False: has not hit a ship

        """
        fired = False
        while not fired:
            loc = input("Please enter where to hit target (i.e A1)")
            if len(loc) == 2 and loc[0].isalpha() and loc[1].isdigit() and self.other_player.board.been_shot(loc):
                hit = self.other_player.update(loc)

                fired = True
                return hit
            else:
                print("Invalid Coordinate, Try again")

    def attempt_fire(self, loc_str):
        """Programmatically attempt to fire on the other player's board

        Args:
            loc_str: the location string to fire at

        Returns:
            True: if we hit
            False: if we miss or invalid
        """
        if loc_string_is_valid(loc_str) and self.other_player.board.cell_can_be_fired_upon(loc_str):
            return self.other_player.update(loc_str)

        return False

    def update(self, loc):
        """ Updates the board and the ship array

        Returns:
            True: a Ship has been hit
            False: a ship has not been Hit
        """

        hit = self.board.update(loc)

        for ship in self.ships:
            if ship.check_if_at_location(loc):
                ship.hit(loc)

        return hit

    def check_other(self, x, y):
        for i in range(9):
            for ii in range(9):
                if self.other_player.board.board[i][ii] == BoardCellState.Ship:
                    print("O")
                else:
                    print(self.other_player.board.board[i][ii])
                    return self.other_player.board.board[i][ii]
            print("\n")
        return self.other_player.board.board

    def check_mine(self):
        for i in range(9):
            for ii in range(9):
                print(self.board.board[i][ii])
            print("\n")
        return self.board.board

    def choose_coordinates(self, i):
        print("Choose the coordinates for the front of the ship. "
              "To orient the ship, you will pivot around this point\n")

        while True:
            x = input("Choose a column:\n\n| A | B | C | D | E | F | G | H | I |\n")
            if (x == "A") | (x == "a"):
                col = "A"
            elif (x == "B") | (x == "b"):
                col = "B"
            elif (x == "C") | (x == "c"):
                col = "C"
            elif (x == "D") | (x == "d"):
                col = "D"
            elif (x == "E") | (x == "e"):
                col = "E"
            elif (x == "F") | (x == "f"):
                col = "F"
            elif (x == "G") | (x == "g"):
                col = "G"
            elif (x == "H") | (x == "h"):
                col = "H"
            elif (x == "I") | (x == "i"):
                col = "I"
            else:
                print("Location is not on the board. Try again\n")
                return False
            os.system("cls")
            y = input("Choose a row:\n\n| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |\n")
            if y == "1":
                row = "1"
            elif y == "2":
                row = "2"
            elif y == "3":
                row = "3"
            elif y == "4":
                row = "4"
            elif y == "5":
                row = "5"
            elif y == "6":
                row = "6"
            elif y == "7":
                row = "7"
            elif y == "8":
                row = "8"
            elif y == "9":
                row = "9"
            else:
                print("Location is not on the board. Try again\n")
                return False
            os.system("cls")
            coordinate = col + row
            front_col = self.letters.index(coordinate[0]) + 1
            front_row = int(coordinate[1])
            orientation = input("Orient Up (U), Down (D), Left (L), or Right (R)?\n")
            if (orientation == "U") | (orientation == "u"):
                back_col = front_col
                back_row = front_row - (self.ships[i] - 1)
                if back_row < 1:
                    print("Ship is off the board by ", -1 * back_row + 1, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(back_row, front_row + 1):
                    if self.board.board[front_col - 1][j - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            elif (orientation == "D") or (orientation == "d"):
                back_col = front_col
                back_row = front_row + (self.ships[i] - 1)
                if back_row > 9:
                    print("Ship is off the board by ", back_row - 9, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(front_row, back_row + 1):
                    if self.board.board[front_col - 1][j - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            elif (orientation == "L") or (orientation == "l"):
                back_col = front_col - (self.ships[i] - 1)
                back_row = front_row
                if back_col < 1:
                    print("Ship is off the board by ", -1 * back_col + 1, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(back_col, front_col + 1):
                    if self.board.board[j - 1][front_row - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            elif (orientation == "R") or (orientation == "r"):
                back_col = front_col + (self.ships[i] - 1)
                back_row = front_row
                if back_col > 9:
                    print("Ship is off the board by ", back_col - 9, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(front_col, back_col + 1):
                    if self.board.board[j - 1][front_row - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            else:
                print("Invalid orientation selection! Choices are: U, D, L, R\n")
                return False
            return self.letters[front_col - 1] + str(front_row) + self.letters[back_col - 1] + str(back_row)

    def place_ship(self, i, front_loc, back_loc):
        self.ships.pop(i)
        self.ships.insert(i, Ship(i + 1, front_loc, back_loc))
        self.board.setUp(self.ships[i])

    def set_ships(self, num_ships=None):  # set the ships on the board by handing the coordinates over to the board class
        if num_ships is not None:
            for i in range(num_ships):
                self.ships.append(i + 1)
        else:
            # TODO remove once GUI
            while True:
                x = input("How many ships do you want to play with?\n")
                os.system("cls")
                if x == "1" or x == "2" or x == "3" or x == "4" or x == "5":
                    x = int(x)
                    for i in range(x):
                        self.ships.append(i + 1)
                    break
                else:
                    print("Invalid number of ships! You can only have 1-5.\n")
            for i in range(len(self.ships)):
                while True:
                    final_location = self.choose_coordinates(i)
                    if not final_location:
                        continue
                    else:
                        break
                front_loc = final_location[0] + final_location[1]
                back_loc = final_location[2] + final_location[3]
                self.place_ship(i, front_loc, back_loc)
