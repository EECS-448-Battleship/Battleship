import os 
from .Player import Player
# this will help with cross platfrom color output
import colorama

# Handels the output for the application
class Terminal:

    def __init__(self):
        # Initialize the cross platform color tool
        colorama.init(autoreset=True)
        
        self.line = 50

    
    def playerView(self, player, enemy):
        print(colorama.Fore.CYAN + "-"*self.line)
        print("Your Board")
        print("----------")
         
        print(colorama.Fore.CYAN + "-"*self.line)

        pass

    def printSwitchPrompt(self, player):

        # Clear the board and other info from the screen
        self.clearScreen()

        print(colorama.Fore.CYAN +"="*self.line)
        print("Its Time to switch")
        print(colorama.Fore.CYAN +"="*self.line)

        

    def printHit(self, loc):
        
        print(colorama.Fore.GREEN +"-"*self.line)
        print(colorama.Fore.GREEN + "The shot at location ("+str(loc[0]) + "," + str(loc[1]) +") was a hit!")
        print(colorama.Fore.GREEN +"-"*self.line)
        

    def printMiss(self, loc):
        
        print(colorama.Fore.RED +"-"*self.line)
        print(colorama.Fore.RED + "The shot at location ("+str(loc[0]) + "," + str(loc[1]) +") was a miss!")
        print(colorama.Fore.RED +"-"*self.line)
        

    def printWinner(self, winPlayer, losePlayer):
        print(colorama.Fore.MAGENTA +"="*self.line)
        print(colorama.Fore.MAGENTA + "The Player " + winPlayer.name + " has Won!!")
        print(colorama.Fore.MAGENTA +"="*self.line)
        pass


    def clearScreen(self):
        
        if(os.name == "nt"):
            os.system('cls')
        elif  (os.name == 'posix'):
            os.system('clear')

