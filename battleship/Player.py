#-------------INDEX OF CLASS: PLAYER METHODS BELOW-------------------
# 
#                      def set_other_player(self, player2)
#action                def fire(self)
#action                def set_ships(self)
#action                def choose_coordinates(self, i)
#bool                  def isFloating(self)
#Prints(str,str)       def check_other(self, x, y):
#Prints()              def check_mine(self):
#---------------PLAYER METHODS END---------------------------------

#Keep in mind, letters MUST be enetered as capital letters
#When calling Player Object, name of player must be passed in.
#There, it will create unique board of the respective player.
#-----------------START OF EXAMPLE USE-------------

#playerObject= Player(Jasmine)
#playerObject= Player(Thomas)
#if playerOne.isFloating() == false:
#print("   Player 2 has won ! ! !")
#choose_coordinates(self, 2)
#object.check_other(self, A, 1):
#object.check_mine(self):
#--------------------------END OF EXAMPLES
import os
from Ship import Ship
from board import board

class Player:

    def __init__(self, name):
    
        self.ships = []
        self.board = board()
        self.name = name
        self.other_player = None
        self.letters = [ "A", "B", "C", "D", "E", "F", "G", "H", "I" ]


    def set_other_player(self, player2):
        self.other_player = player2


    def isFloating(self):
        for i in range(len(self.ships)):
            for ii in range(self.ships.isHit_array[i]):
                if self.ships[i].isHit_array[ii] == False:
                    return True
        return False


    def fire(self):                                                        #to fire at other players ships
        """ 
        
        """
        col = input("Please enter where to hit target (column)")
        row = input("Please enter where to hit target (row)")
        self.other_player.board.update(col+row)
        return self.other_player.board.update(col+row)



    def check_other(self, x, y):                                                 #check if you have fired at a specific location
        
        for i in range(9):
            for ii in range(9):
                if self.other_player.board.board[i][ii] == "S":
                    print("O")
                else:
                    print(self.other_player.board.board[i][ii])
            print("\n")



    def check_mine(self):                                                        #check what ships have been hit
        for i in range(9):
            for ii in range(9):
                print(self.board.board[i][ii])
            print("\n")



    def choose_coordinates(self, i):                                                #method to choose coordinates of the front of the ship
    
        print("Choose the coordinates for the front of the ship. "
        "To orient the ship, you will pivot around this point\n")
        while ( True ):
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
                if (back_row < 1):
                    print("Ship is off the board by ", -1*back_row + 1, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(back_row, front_row + 1):
                    if self.board.board[front_col - 1][j - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            elif (orientation == "D") | (orientation == "d"):
                back_col = front_col
                back_row = front_row + (self.ships[i] - 1)
                if (back_row > 9):
                    print("Ship is off the board by ", back_row-9, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(front_row, back_row + 1):
                    if self.board.board[front_col - 1][j - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            elif (orientation == "L") | (orientation == "l"):
                back_col = front_col - (self.ships[i] - 1)
                back_row = front_row
                if (back_col < 1):
                    print("Ship is off the board by ", -1*back_col + 1, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(back_col, front_col + 1):
                    if self.board.board[j - 1][front_row - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            elif (orientation == "R") | (orientation == "r"):
                back_col = front_col + (self.ships[i] - 1)
                back_row = front_row
                if (back_col > 9):
                    print("Ship is off the board by ", back_col - 9, " space(s)! Try another orientaion.\n")
                    return False
                for j in range(front_col, back_col + 1):
                    if self.board.board[j - 1][front_row - 1] == "S":
                        print("A ship is already located here! Try another orientation.\n")
                        return False
            else:
                print("Invalid orientaion selection! Choices are: U, D, L, R\n")
                return False
            return self.letters[front_col - 1] + str(front_row) + self.letters[back_col - 1] + str(back_row)    
    
    

    def set_ships(self):                                                                         #set the ships on the board by handing the coordinates over to the board class    
    
        while ( True ):        
            x = input("How many ships do you want to play with?\n")
            os.system("cls")
            if (x == "1") | (x == "2") | (x == "3") | (x == "4") | (x == "5"): 
                x = int(x)
                for i in range(x):
                    self.ships.append(i+1)
                break
            else:
                print("Invalid number of ships! You can only have 1-5.\n")
        for i in range(len(self.ships)):
            while (True):
                final_location = self.choose_coordinates(i)
                if final_location == False:
                    continue
                else:
                    break
            front_loc = final_location[0] + final_location[1]
            back_loc = final_location[2] + final_location[3]
            self.ships.pop(i)
            self.ships.insert(i, Ship(i + 1, front_loc, back_loc))
            self.board.setUp(self.ships[i])
            
