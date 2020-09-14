from .Ship import Ship
from .Player import Player
from .board import board
from .terminal import Terminal

class Game:
	""" The class 

	Attributes:
		p1: The first player object.
		p2: The second player object.
		aTerminal: The terminal helper object.


	"""
	aTerminal = Terminal()

	def __init__(self):
		"""
		Initializes the game

		"""
		self.aTerminal.printWelcome()
		
		player_one_name = input("Player 1, please enter your name: ")
		self.p1 = Player(player_one_name)
		self.p1.set_ships()
		self.aTerminal.printSelfBoard(self.p1.board)

		input("Press enter to Contitue")
		self.aTerminal.clearScreen()

		player_two_name = input("Player 2, please enter your name: ")
		self.p2 = Player(player_two_name)
		self.p2.set_ships()
		self.aTerminal.printSelfBoard(self.p2.board)


		self.p1.other_player = self.p2
		self.p2.other_player = self.p1


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
			
			hit = self.p1.fire()
			
			if hit:
				self.aTerminal.printHit()
			else:
				self.aTerminal.printMiss()
			
			input()

			#checks if player's boats are floating
			if(self.p2.board.any_left()==False):
				won_game==True
				self.aTerminal.printWinner(self.p1,self.p2)
				break
			
			if won_game==False:	
				#players switch
				self.aTerminal.printSwitchPrompt(self.p2)
				
				
				#board of player two is shown and chooses target area to hit
				self.aTerminal.playerView(self.p2,self.p1)
				#player_two_board.print_board()
				hit = self.p2.fire()

				if hit:
					self.aTerminal.printHit()
				else:
					self.aTerminal.printMiss()
				
				input()
				
				#checks if player's boats are floating
				if(self.p1.board.any_left()==False):
					won_game==True
					self.aTerminal.printWinner(self.p2,self.p1)
					break			
				self.aTerminal.printSwitchPrompt(self.p1)	
	