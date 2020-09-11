
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
        
        self.hit_array=[False*(self.length)]
        self.board_array=[None*(self.length)]
        
     
        if self.front[0] == self.back[0]:
            
            self.orientation="h"

        else:
            self.orientation="v"
            self.hitarray=[False]


        if self.orientation == "h":
            int(self.front[1])
            int(self.back[1])

            for i in range(0,self.length):
                
                if i ==0:
                    self.board_array[i]=self.front
                
                if i == self.length:
                    self.board_array[i]=self.back
                
                else:





  




    #def isHit(self, location):
     

     
    
    def hit(self,location):
        self.health=self.health-1
        for i in range(0,self.length):
            

    
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








Barco=Ship(3, "B2", "B5")
print(Barco.health)
Barco.hit()
print(Barco.health)
Barco.getlocation()
print(Barco.array[0])
print(Barco.array)
print(Barco.front[1],Barco.front[0],Barco.back[1], Barco.front)


