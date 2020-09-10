
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
        self.array=[6]
        if self.length == 1:
            {}
        else:
           {}
    
    def hit(self):
        self.health=self.health-1
    
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

    def isHit(self):
        {}



Barco=Ship(3, "B2", "B5")
print(Barco.health)
Barco.hit()
print(Barco.health)
Barco.getlocation()
