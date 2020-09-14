#-------------INDEX OF CLASS: SHIP METHODS BELOW-------------------
# 
#                      def __init__(self, length, front, back)
#bool                  def isHit(self, location)
#action                def hit(self,location)
#bool                  def isFloating(self)
#int                   def getHealth(self)
#int                   def getSize(self)
#Prints(str,str)       def getlocation(self)
#
#---------------SHIP METHODS END---------------------------------

#Keep in mind, letters MUST be enetered as capital letters
#will place "front" of ship and "back" in an order that goes from
#1) First to last letter by order of alphabet 
#2) Smallest to largest by int 

# Example: (B6,B2) are input by user, if Ship.getlocation() is called
#       it will output (B2,B6), front and back are switched when 
#       ___init__ is called




# Examples of Functions in use, this is how I tested everything
#-----------------START OF EXAMPLE USE-------------

#Ship_Ex=Ship(4, "F2", "C2")
#Ship_Ex.hit("E2")
#Ship_Ex.hit("C2")
#Ship_Ex.hit("D2")
#Ship_Ex.hit("F2")
#loc="E2"
#loc2="C2"
#if Ship_Ex.isHit(loc) == True:
#    print(loc,"is hit method positive")
#else:
#    print(loc,"is hit method false")

#if Ship_Ex.isHit(loc2) == True:
#    print(loc2,"is hit method")
#else:
#    print(loc2,"is hit method false")   

#if Ship_Ex.isFloating()==True:
#    print("Boat is still up")
#elif Ship_Ex.isFloating()==False:
#    print("boat ded")

#print(Ship_Ex.isHit_array[0])
#print(Ship_Ex.isHit_array[1])
#print(Ship_Ex.getHealth())
#print(Ship_Ex.getSize())
#Ship_Ex.getlocation()
#--------------------------END OF EXAMPLES

class Ship:
    """Ship class which is used when building a ship from player class.

    Ship object is instantiated when the player class calls on an object to be
    created. This class takes in length of the boat and from where to where (point A
    and point B) on the board the ship is at.
    
    Locations are taken in as strings which are then arranged by the __init__ method when 
    the ship object is constructed.
    
    """
    def __init__(self, length, front, back):
        
        """ Constructs Ship object, arranges front and back locations and takes in length.

        Arguments taken from Player:
            length:
                This is how long the boat is, 1x1 length 1, 1x4 length 4
            front:
                String argument is the location of the front of the ship
            back:
                String argument is the location of the back of the ship
        
        Actions:
            init creates class variables:
                self.health- int that represents the health of the boat
                self.length- int that represents the length of the ship
                self.front- string which is location of front of the ship
                self.back- string that is location of back of the ship
            
            init also creates arrays:
                self.isHit_array- a bool array the length of the ship holding if the ship   "has been hit" or not
                self.board_array- a str array the length of the ship which holds the locations of the boat
                    EX- Front-B3 Back-B5 then
                        self.board_array[0]=B3
                        self.board_array[1]=B4
                        self.board_array[2]=B5
            
            After the above is done it will then figure out what orientation
            the boat is facing and then see that self.front and self.back are in proper location
            Arguments "front" and "back" are passed by the player, the code after arrays
            make sure that they are in order from 
                1)Smallest row integer
                    OR
                2)Alphabetical column order 
            Ex:
                Player passes Ship1.Ship(2, "B2", "B1")
                front is passed as B2 and back is passed as B1.
                The code will say self.orientation="h" (for horizontal)
                self.front = "B1" 
                self.back = "B2"

        Call:
            Makes a call to fill_location_array which then fills in self.board_array

        """
        self.health=length
        self.length=length
        self.front=front
        self.back=back
        
        self.isHit_array=[False]*(self.length)
        self.board_array=[("")]*(self.length)


#Bottom will put the input in order from smallest to largest number
        if self.front[0] == self.back[0]:
            
            self.orientation="h"
            self.front_int= int(self.front[1])
            self.back_int=int(self.back[1])
            
            if self.front_int>self.back_int:
                self.front=back
                self.back=front
        
                self.front_int= int(self.front[1])
                self.back_int=int(self.back[1])
#Bottom half of if statement will then activate if the orientation is horizontal
#which will put in order of smallest (A) to largest (I)
        elif self.front[0] != self.back[0]:
            self.orientation="v"

            if self.column_to_num(self.front[0]) > self.column_to_num(self.back[0]):
                self.front=back
                self.back=front


        self.fill_location_array(self.orientation)           





#Below bool isHit function
    def isHit(self, location):

        """bool function that returns true or false for if ship is hit.

        Arg:
            Takes in str "location"

        Summary:
            It checks all locations entered in the board_array and once it gets a hit 
            it will see if the isHit_array returns true.
            WHAT THIS MEANS IS, the player already called a hit function and that location of 
            where the ship was placed, has been hit


        """

        for i in range(0,self.length):
            if self.board_array[i]==location:
                if self.isHit_array[i] == True:
                    return True
                else:
                    return False
           

#Function below to fill in board_array
    def fill_location_array(self, orientation):

        """Fills self.board_array with locations.

        Args:
            orientation- a string that holds if the range of board locations is facing up and down OR 
                            left and right
        
        Action:
            if orientation = "h":
                Then it will take the self.front[1] and self.back[1] variables and, in a for loop, will continuously add a 
                rising number "i" in range from 0 to the length of the ship. It will take the number part of the coordinate, which is a string,
                then it will change it to an int, add it to what the current "i" integer in the for loop is and make it back in to a string, concatinating
                it right after the letter part of the coordinate which is then added to self.board_array[i]

            
            if orientation = "v":
                Then it will take the letter component of the location and convert it to an int, with column_to_num.
                As the for loop starts, the number representation of the the letter will raise by adding "i" to the int representation,
                this is to fill in self.board_array with the range of front and back. This int being raised will be changed back to 
                to a letter and then will proceed to be added to the board_array.

        """

#Bottom method will verify that orientation is horizontal
#then will input the location into the board array index [i]
      
        if self.orientation=="h":
            for i in range(0,self.length):

                if i ==0:
                    self.board_array[i]=self.front

                if i < self.length-1:
                    temp=str((int(self.front[1])+i))
                    front_str=self.front[0]+temp
                    self.board_array[i] = front_str


                if i==(self.length)-1:
                    self.board_array[i]=self.back

        
        elif self.orientation=="v":
            for i in range(0, (self.length)):
                temp=self.column_to_num(self.front[0])
                index_num=temp+i
                
                self.board_array[i]=self.back_to_row(index_num)+self.front[1]
                        



    def hit(self,location):
        """Player passes location, this will lower the health of the ship.

        Arg:
            location-str containing location of where the player wants to hit the other players ship
        Action:
            This will be in a for loop checking if the location passed in matches with
            location saved in the board_array. It will then check the isHit array of the corresponding "i"
            and will bring the health count down by one if the ship hasn't been hit yet or it will print out 
            "already hit" message

        """
        for i in range(0,self.length):
            if self.board_array[i]==location:
                if self.isHit_array[i]==False:
                    self.isHit_array[i] = True
                    self.health=self.health-1  
                    print(location, "has been hit")
                else:
                    print("Location has already been hit")


                    
    
    def isFloating(self):
        """Bool Function returns true if boat is health is above 0, returns false if sunk.
        
        """
        if self.health>0:
            return True
        else:
            return False

    def getHealth(self):
        """returns int which represents the ship's current health.
        """
        return self.health
 
    def getSize(self):
        """returns int representing the length of the ship.
        """
        return self.length

    def getlocation(self):
        """Prints out the location of the ship, front and back.
        """
        print("(Front,Back) of Ship: ", "(",self.front, ",", self.back,")")

    def column_to_num(self, str):
        """Used by fill_location_array method to change letter to number.

        Args:
            str- this represents the letter of the coordinate passed in
        Actions:
            str is checked to match ones of these, once matched it will return the corresponding
            int.
        """
        if str=="A":
            return 1
        if str=="B":
            return 2
        if str=="C":
            return 3
        if str=="D":
            return 4
        if str=="E":
            return 5
        if str=="F":
            return 6
        if str=="G":
            return 7
        if str=="H":
            return 8
        if str=="I":
            return 9

    def back_to_row(self, int):
        """Used by fill_location_array method to change number back to letter.

        Args:
            int-this will return the letter turned into an int back into a letter
        Actions:
            int is checked for corresponding number, once found it will return the corresponding
            letter
        """
        if int == 1:
            return "A"
        if int == 2:
            return "B"
        if int == 3:
            return "C"
        if int == 4:
            return "D"
        if int == 5:
            return "E"
        if int == 6:
           return "F"
        if int == 7:
            return "G"
        if int == 8:
            return "H"
        if int == 9:
            return "I"

    def get_location_array(self):
        """Returns the locations of the ship.
        """
        return self.board_array


