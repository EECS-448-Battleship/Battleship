import os
from class_ship import Ship

class Player:

    def __init__(self, name):
    
        self.ships = []
        self.name = name
        self.letters = [ "A", "B", "C", "D", "E", "F", "G", "H", "I" ]



    def fire(self):                                                        #to fire at other players ships
        """ 
        

        """
        hit_successful = False

        while not hit_successful:
            col = input("Player1, please enter where to hit target (column)")
			row = input("Please enter where to hit target (row)")

            if board(x,y) & board.is_hit(x,y):
                # If the board has a ship there                                #if a ship is there and it has been hit
                print("Location already hit.")
                return False
            elif board.filled(x,y) & board.is_not_hit(x,y):                          #if a ship is there and it has not been hit
                print("Hit!")
                return True
            elif board.not_filled(x,y):                                              #if a ship is not there
                print("Miss!")
                return False



    def check_other(self, x, y):                                                 #check if you have fired at a specific location
   
        if board.is_hit(x,y):
            return True
        else:
            return False



    def check_mine(self):                                                        #check what ships have been hit
    
        for x in ships:
            if ships[x].is_hit():
                return True                                                      #need to figure out how we print which ship/location



    def choose_coordinates(self):                                                #method to choose coordinates of the front of the ship
    
        print("Choose the coordinates for the front of the ship. "
        "To orient the ship, you will pivot around this point\n")
        while ( True ):
            x = input("Choose a column:\n\n| A | B | C | D | E | F | G | H | I |\n")
            if (x == "A") | (x == "a"):
                col = "A"
                break
            elif (x == "B") | (x == "b"):
                col = "B"
                break
            elif (x == "C") | (x == "c"):
                col = "C"
                break
            elif (x == "D") | (x == "d"):
                col = "D"
                break
            elif (x == "E") | (x == "e"):
                col = "E"
                break
            elif (x == "F") | (x == "f"):
                col = "F"
                break
            elif (x == "G") | (x == "g"):
                col = "G"
                break
            elif (x == "H") | (x == "h"):
                col = "H"
                break
            elif (x == "I") | (x == "i"):
                col = "I"
                break
            else:
                print("Location is not on the board. Try again\n")
                continue
        os.system("cls")
        while ( True ):
            y = input("Choose a row:\n\n| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |\n")
            if y == "1":
                row = "1"
                break
            elif y == "2":
                row = "2"
                break
            elif y == "3":
                row = "3"
                break
            elif y == "4":
                row = "4"
                break
            elif y == "5":
                row = "5"
                break
            elif y == "6":
                row = "6"
                break
            elif y == "7":
                row = "7"
                break
            elif y == "8":
                row = "8"
                break
            elif y == "9":
                row = "9"
                break
            else:
                print("Location is not on the board. Try again\n")
                continue
        os.system("cls")
        coordinate = col + row
        return coordinate        
    
    
    
    def choose_orient(self, coordinate, i):                                                   #method to choose the orientation of the ship
    
        front_col = self.letters.index(coordinate[0]) + 1
        front_row = int(coordinate[1])
        while ( True ):
            orientation = input("Orient Up (U), Down (D), Left (L), or Right (R)?\n")
            if (orientation == "U") | (orientation == "u"):
                back_col = front_col
                back_row = front_row - (self.ships[i] - 1)
                if (back_row < 1):
                    print("Ship is off the board by ", -1*back_row + 1, " space(s)! Try another orientaion.\n")
                    continue
                break
            elif (orientation == "D") | (orientation == "d"):
                back_col = front_col
                back_row = front_row + (self.ships[i] - 1)
                if (back_row > 9):
                    print("Ship is off the board by ", back_row-9, " space(s)! Try another orientaion.\n")
                    continue
                break
            elif (orientation == "L") | (orientation == "l"):
                back_col = front_col - (self.ships[i] - 1)
                back_row = front_row
                if (back_col < 1):
                    print("Ship is off the board by ", -1*back_col + 1, " space(s)! Try another orientaion.\n")
                    continue
                break
            elif (orientation == "R") | (orientation == "r"):
                back_col = front_col + (self.ships[i] - 1)
                back_row = front_row
                if (back_col > 9):
                    print("Ship is off the board by ", back_col - 9, " space(s)! Try another orientaion.\n")
                    continue
                break
            else:
                print("Invalid orientaion selection! Choices are: U, D, L, R\n")
                continue
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
            initial_location = self.choose_coordinates()
            final_location = self.choose_orient(initial_location, i)
            front_loc = final_location[0] + final_location[1]
            back_loc = final_location[2] + final_location[3]
            self.ships.pop(i)
            self.ships.insert(i, Ship(i + 1, front_loc, back_loc))
            #self.board.place_ship(x,y)





player = Player("Player 1")
player.set_ships()