from .Player import Player
from .AIPlayer import AIPlayer
from .GameEvents import GameEvents


class Game:
	""" The class 

	Attributes:
		p1: The first player object.
		p2: The second player object.
		events: The game event bus.
	"""

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

		# prompt player 1 to choose if player 2 is an AI or real person
		is_ai = self.events.choose_if_ai()

		# Set up player 2 and their board (ai or otherwise)
		if is_ai:
			self.p2 = AIPlayer('Computer')
			self.p2.ai_difficulty = self.events.choose_ai_difficulty()
		else:
			player_two_name = self.events.prompt_player_name()
			self.p2 = Player(player_two_name)

		self.p1.other_player = self.p2
		self.p2.other_player = self.p1

		self.p2.set_ships(num_ships)

		self.events.switch_to_player(self.p1)
		self.events.place_ships(self.p1)

		self.events.switch_to_player(self.p2)
		self.events.place_ships(self.p2)

	def play_game(self):
		"""
		Starts the game
		"""
		won_game = False

		self.events.switch_to_player(self.p1)
	
		while not won_game:
			# board of player one is shown and chooses target area to hit
			p1_fire_loc = self.events.get_fire_coordinates(self.p1)
			p1_hit = self.p1.attempt_fire(p1_fire_loc)

			if p1_hit:
				self.events.show_player_hit(self.p1)
			else:
				self.events.show_player_miss(self.p1)

			# checks if player's boats are floating
			if not self.p2.board.any_left():
				won_game = True
				self.events.show_player_victory(self.p1)

			if not won_game:
				# players switch
				self.events.switch_to_player(self.p2)

				p2_fire_loc = self.events.get_fire_coordinates(self.p2)
				p2_hit = self.p2.attempt_fire(p2_fire_loc)

				if p2_hit:
					self.events.show_player_hit(self.p2)
				else:
					self.events.show_player_miss(self.p2)

				# checks if player's boats are floating
				if not self.p1.board.any_left():
					won_game = True
					self.events.show_player_victory(self.p2)

				if not won_game:
					self.events.switch_to_player(self.p1)
