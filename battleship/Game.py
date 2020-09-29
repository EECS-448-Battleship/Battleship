from .Player import Player
from .AIPlayer import AIPlayer
from .Terminal import Terminal
from .GameEvents import GameEvents


class Game:
	""" The class 

	Attributes:
		p1: The first player object.
		p2: The second player object.
		terminal: The terminal helper object.
		events: The game event bus.
	"""

	terminal = Terminal()
	events = GameEvents()

	def __init__(self):
		"""
		Initializes the game
		"""
		self.events.show_welcome()

		num_ships = self.events.choose_number_of_ships()

		# Fetch player 1's name and set up their board
		player_one_name = self.events.prompt_player_name()
		self.p1 = Player(player_one_name)
		self.p1.set_ships(num_ships)
		self.events.place_ships(self.p1)

		# prompt player 1 to choose if player 2 is an AI or real person
		is_ai = self.events.choose_if_ai()

		# Set up player 2 and their board (ai or otherwise)
		if is_ai:
			self.p2 = AIPlayer('Computer')
			self.p2.set_ships(num_ships)
			# TODO - call place_ships on AIPlayer, not via GUI
		else:
			player_two_name = self.events.prompt_player_name()
			self.p2 = Player(player_two_name)
			self.p2.set_ships(num_ships)
			self.events.place_ships(self.p2)

		self.p1.other_player = self.p2
		self.p2.other_player = self.p1

	def play_game(self):
		"""
		Starts the game
		"""
		won_game = False
	
		while(won_game == False):
			# board of player one is shown and chooses target area to hit
			self.terminal.playerView(self.p1,self.p2)
			# self.player_one_board.print_board(self.p1)
			
			hit = self.p1.fire()
			
			if hit:
				self.terminal.printHit()
			else:
				self.terminal.printMiss()
			
			input()

			# checks if player's boats are floating
			if not self.p2.board.any_left():
				won_game = True
				self.terminal.printWinner(self.p1,self.p2)
				break
			
			if not won_game:
				# players switch
				self.terminal.printSwitchPrompt(self.p2)
				
				# board of player two is shown and chooses target area to hit
				self.terminal.playerView(self.p2,self.p1)
				# player_two_board.print_board()
				hit = self.p2.fire()

				if hit:
					self.terminal.printHit()
				else:
					self.terminal.printMiss()
				
				input()
				
				# checks if player's boats are floating
				if not self.p1.board.any_left():
					won_game = True
					self.terminal.printWinner(self.p2,self.p1)
					break

				self.terminal.printSwitchPrompt(self.p1)	
