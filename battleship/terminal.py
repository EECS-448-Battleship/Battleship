import os 

# this will help with cross platfrom color output
import colorama

# Handels the output for the application
class Terminal:

    def __init__(self):
        # Initialize the cross platform color tool
        colorama.init(autoreset=True)
        
        self.line = 50

    
    def printBoard(self, board):
        
        pass

    def printSwitchPrompt(self, player):

        # Clear the board and other info from the screen
        self.clearScreen()

        print(colorama.Fore.CYAN +"="*self.line)
        print("Its Time to switch")
        print(colorama.Fore.CYAN +"="*self.line)

        

    def printHit(self, loc):
        
        print(colorama.Fore.GREEN +"-"*self.line)
        print(colorama.Fore.GREEN + "The shot at location ("+loc[0] + "," + loc[1] +") was a hit!")
        print(colorama.Fore.GREEN +"="*self.line)
        

    def printMiss(self, loc):
        
        print(colorama.Fore.RED +"-"*self.line)
        print(colorama.Fore.RED + "The shot at location ("+loc[0] + "," + loc[1] +") was a miss!")
        print(colorama.Fore.RED +"="*self.line)
        

    def printWinner(self, winPlayer, losePlayer):
        pass


    def clearScreen(self):
        
        if(os.name == "nt"):
            os.system('cls')
        elif  (os.name == 'posix'):
            os.system('clear')
    