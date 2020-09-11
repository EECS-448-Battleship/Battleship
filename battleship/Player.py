class Player:

    def __init__(self, ships, board, name):
        self.ships = ships
        self.board = board
        self.name = name

#fire at other players ships
    def fire(x, y):
        #if a ship is there and it has been hit
        if board.filled(x,y) & board.is_hit(x,y):
            print("Location already hit.")
            return False
        #if a ship is there and it has not been hit
        elif board.filled(x,y) & board.is_not_hit(x,y):
            print("Hit!")
            return True
        #if a ship is not there
        elif board.not_filled(x,y):
            print("Miss!")
            return False

#check if you have fired at a specific location
    def check_other(x, y):
        if board.is_hit(x,y):
            return True
        else:
            return False

#check what ships have been hit
    def check_mine():
        for x in ships:
            if ships[x].is_hit():
                print("Ship has been hit at ")  #need to figure out how we print which ship/location

#set the ships on the board
    def set_ships():
        for i in ships:
            x = 0
            y = 0
            while ((x > 9 | x < 1) & (y > 9 | y < 1)):
                print("Enter an x location\n")
                x = input()
                print("Enter a y location\n")
                y = input()
                if ((x > 9 | x < 1) & (y > 9 | y < 1)):
                    print("location is not on the board.\n")
            board.place_ship(x,y)                                       #Not sure if we should allow for ship orientation in player class or board class


