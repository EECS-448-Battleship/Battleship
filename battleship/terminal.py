import os 
import Player
import board
# this will help with cross platfrom color output
import colorama

# Handels the output for the application
class Terminal:

    def __init__(self):
        # Initialize the cross platform color tool
        colorama.init(autoreset=True)
        
        self.line = 50

    
    def playerView(self, player, enemy):
        """
        This function prints the players view

        @parm player is the player object whos turn it is
        @parm enemy is the player object whos turn it is not
        """

        print(colorama.Fore.CYAN + "-"*self.line)

        self.printSelfBoard(player.board)
        print(colorama.Fore.CYAN + "-"*self.line)

        self.printOtherBoard(enemy.board)

        print(colorama.Fore.CYAN + "-"*self.line)


    
    def printSelfBoard(self, board):
        """
        This function prints the  players board

        @parm board is the board to print
        """
        
        print("Your Board")
        print("-"*18)

        for row in board.board:
            for loc in row:
                if loc == 'O':
                    print(colorama.Fore.BLUE + "O", end=" ")
                elif loc == 'S':
                    print(colorama.Fore.GREEN + "S", end=" ")
                elif loc == 'X':
                    print(colorama.Fore.RED + "X", end=" ")
                elif loc == '*':
                    print(colorama.Fore.MAGENTA + "*", end= " ")
            print("")

    def printOtherBoard(self, board):
        """
        This function prints the other players board

        @parm board is the board to print
        """

        print("Your Enemies Board")
        print("-"*18)

        for row in board.board:
            for loc in row:
                if loc == 'O' or loc == 'S':
                    print(colorama.Fore.BLUE + "O", end=" ")
                elif loc == 'X':
                    print(colorama.Fore.RED + "X", end=" ")
                elif loc == '*':
                    print(colorama.Fore.MAGENTA + "*", end= " ")
            print("")

    def printWelcome(self):
        # Clear the board and other info from the screen
        self.clearScreen()

        print(colorama.Fore.CYAN +"="*self.line)
        print("Welcome to the game. Players will take turns.")
        print("When it is not your turn please look away!")
        print(colorama.Fore.CYAN +"="*self.line)

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

