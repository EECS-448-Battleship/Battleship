#-------------INDEX OF CLASS: SHIP METHODS BELOW-------------------
# 
#                      def __init__(self, length, front, back)
#bool                  def isHit(self, location)
#action                def hit(self,location)
#bool                  def isFloating(self)
#int                   def getHealth(self)
#int                   def getSize(self)
#Prints(str,str)       def getlocation(self)
#                      def get_location_array(self):
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
#Ship_Ex.get_location_array()
#--------------------------END OF EXAMPLES

# Variables in parameter of "__init__"
# Front and Back are locations, example placing 1x2 ship on 
# Front:B2 and Back:B4
# When making location, in example "B2" I took it to be a string and not a character+int

class Ship:
    def __init__(self, length, front, back):
        
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
        for i in range(0,self.length):
            if self.board_array[i]==location:
                if self.isHit_array[i] == True:
                    return True
                else:
                    return False
           

#Function below to fill in board_array
    def fill_location_array(self, orientation):


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
                
                self.board_array[i]=self.back_to_column(index_num)+self.front[1]
                        



    def hit(self,location):
        
        for i in range(0,self.length):
            if self.board_array[i]==location:
                if self.isHit_array[i]==False:
                    self.isHit_array[i] = True
                    self.health=self.health-1  
                    print(location, "has been hit")
                else:
                    print("Location has already been hit")


                    
    
    def isFloating(self):
        if self.health>0:
            return True
        else:
            return False

    def getHealth(self):
        return self.health
 
    def getSize(self):
        return self.length

    def getlocation(self):
        print("(Front,Back) of Ship: ", "(",self.front, ",", self.back,")")

    def column_to_num(self, str):
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

    def back_to_column(self, int):
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
        return self.board_array







