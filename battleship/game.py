from class_ship.py import Ship
from Player.py import Player
from board.py import board
from terminal.py import Terminal

class Game:

	def __init__(self)
		player_one_name =''
		player_two_name= ''
		
	#begins the game & conducts turn untill winner determined
	def play_game(self)
		won_game = false;
	
		while(won_game==false)
			
				
			#board of player one is shown and chooses target area to hit 
			aTerminal.playerView(p1,p2)
			player_one_board.print_board(p1)
			col = input("Player1, please enter where to hit target (column)")
			row = input("Please enter where to hit target (row)")
			p1.fire(col,row)
			
			#checks if player's boats are floating
			if(p2.isFloating()==false)
				aTerminal.printWiner(p1,p2)
				break()	
				
			#players switch
			aTerminal.printSwitchPrompt(p2)
			
			
			#board of player two is shown and chooses target area to hit
			aTerminal.playerView(p2,p1)
			player_two_board.print_board()
			col = input("Player2, please enter where to hit target (column)")
			row = input("Please enter where to hit target (row)")
			p1.fire(col,row)
			
			#checks if player's boats are floating
			if(p1.isFloating()==false)
				aTerminal.printWiner(p2,p1)
				break()			
			aTerminal.printSwitchPrompt(p1)	
	
	
aTerminal = Terminal()

player_one_name = input("Player 1, please enter your name: ")
p1 = Player(player_one_name)
p1.set_ships()
player_one_board = board()

aTerminal.clearScreen()

player_two_name = input("Player 2, please enter your name: ")
p2 = Player(p2Name)
p2.set_Ships()
player_two_board= board()

aTerminal.clearScreen()

self.play_game()