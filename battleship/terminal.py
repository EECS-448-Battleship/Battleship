import os 
from .Player import Player
from .board import board
# this will help with cross platfrom color output
import colorama

# Handels the output for the application
class Terminal:
    """This is a helper class that will help print to the terminal

    Attributes:
        line: the length of the line that sepreates the sections
    """

    def __init__(self):
        # Initialize the cross platform color tool
        colorama.init(autoreset=True)
        
        self.line = 50

    
    def playerView(self, player, enemy):
        """
        This function prints the players view

        Args:
            player: the player object whos turn it is
            enemy: the player object whos turn it is not
        """

        print(colorama.Fore.CYAN + "-"*self.line)

        self.printSelfBoard(player.board)
        print(colorama.Fore.CYAN + "-"*self.line)

        self.printOtherBoard(enemy.board)

        print(colorama.Fore.CYAN + "-"*self.line)


    
    def printSelfBoard(self, board):
        """
        This function prints the  players board
        
        Args:   
            board: the board to print
        """
        
        print("Your Board")
        print("-"*20)


        print("  A B C D E F G H I")
        index = 1

        for row in board.board:
            print(index,  end=" ") 
            index += 1
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

        Args:
            board: the board to print
        """

        print("Your Enemies Board")
        print("-"*20)

        print("  A B C D E F G H I")
        index = 1

        for row in board.board:
            print(index,  end=" ") 
            for loc in row:
                if loc == 'O' or loc == 'S':
                    print(colorama.Fore.BLUE + "O", end=" ")
                elif loc == 'X':
                    print(colorama.Fore.RED + "X", end=" ")
                elif loc == '*':
                    print(colorama.Fore.MAGENTA + "*", end= " ")
            print("")

    def printWelcome(self):
        """Prints the Welcome message to the players
        
        """
        
        # Clear the board and other info from the screen
        self.clearScreen()

        print(colorama.Fore.CYAN +"="*self.line)
        print("Welcome to the game. Players will take turns.")
        print("When it is not your turn please look away!")
        print(colorama.Fore.CYAN +"="*self.line)

    def printSwitchPrompt(self, player):
        """
        Prints the promt to switch players 

        Args:
            player: the player whos turn it is
        """

        # Clear the board and other info from the screen
        self.clearScreen()

        print(colorama.Fore.CYAN +"="*self.line)
        print("Its Time to switch to "+ player.name)
        input("Press Enter to continue")
        print(colorama.Fore.CYAN +"="*self.line)
        

    def printHit(self, loc):
        """
        Prints that a location was a hit

        Args:        
            loc: The tupple of the location 
        """
        print(colorama.Fore.GREEN +"-"*self.line)
        print(colorama.Fore.GREEN + "The shot at location ("+str(loc[0]) + "," + str(loc[1]) +") was a hit!")
        print(colorama.Fore.GREEN +"-"*self.line)
        

    def printMiss(self, loc):
        """
        Prints that a location was a miss
        
        Args:
            loc: the tupple of the location 
        """
        print(colorama.Fore.RED +"-"*self.line)
        print(colorama.Fore.RED + "The shot at location ("+str(loc[0]) + "," + str(loc[1]) +") was a miss!")
        print(colorama.Fore.RED +"-"*self.line)
        

    def printWinner(self, winPlayer, losePlayer):
        """
        Prints the winner
        
        Args:
            winPlayer: the player who won
            losePlayer: the player who lost
        """
        print(colorama.Fore.MAGENTA +"="*self.line)
        print(colorama.Fore.MAGENTA + "The Player " + winPlayer.name + " has Won!!")
        print(colorama.Fore.MAGENTA +"="*self.line)
        pass


    def clearScreen(self):
        """
        A function to clear the screen that will work on windows, macOS, or linux

        """
        if(os.name == "nt"):
            os.system('cls')
        elif  (os.name == 'posix'):
            os.system('clear')

