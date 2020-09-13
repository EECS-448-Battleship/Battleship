from class_ship import Ship
from Player import Player
from board import board
from Terminal import Terminal

class Game:

	def __init__(self):
		"""
		Initializes the game

		"""
		self.aTerminal = Terminal()
		self.aTerminal.printWelcome()
		
		player_one_name = input("Player 1, please enter your name: ")
		self.p1 = Player(player_one_name)
		self.p1.set_ships()
		self.aTerminal.printSelfBoard(self.p1.board)


		player_two_name = input("Player 2, please enter your name: ")
		self.p2 = Player(player_two_name)
		self.p2.set_ships()
		self.aTerminal.printSelfBoard(self.p2.board)

		input("Press enter to begin")
		self.aTerminal.clearScreen()


		
	#begins the game & conducts turn untill winner determined
	def play_game(self):
		"""
		Startes the game 
		"""

		won_game = False
	
		while(won_game==False):
			
				
			#board of player one is shown and chooses target area to hit 
			self.aTerminal.playerView(self.p1,self.p2)
			#self.player_one_board.print_board(self.p1)
			col = input("Player1, please enter where to hit target (column)")
			row = input("Please enter where to hit target (row)")
			self.p1.fire(col,row)
			
			#checks if player's boats are floating
			if(self.p2.isFloating()==False):
				won_game==True
				self.aTerminal.printWinner(self.p1,self.p2)
				break
				
			#players switch
			self.aTerminal.printSwitchPrompt(p2)
			
			
			#board of player two is shown and chooses target area to hit
			self.aTerminal.playerView(self.p2,self.p1)
			#player_two_board.print_board()
			col = input("Player2, please enter where to hit target (column)")
			row = input("Please enter where to hit target (row)")
			self.p1.fire(col,row)
			
			#checks if player's boats are floating
			if(self.p1.isFloating()==False):
				won_game==True
				self.aTerminal.printWinner(self.p2,self.p1)
				break			
			self.aTerminal.printSwitchPrompt(self.p1)	
	

g = Game()

g.play_game()
