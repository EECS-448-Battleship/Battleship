from .Terminal import Terminal
from .AIPlayer import AIPlayer
from .GUI.Window import Window

import time


class GameEvents:
    terminal = Terminal()
    window = Window()

    welcome_message = '\n \n'.join([
        'You will get started by choosing the number of ships you want to play with.',
    ])

    def show_welcome(self):
        # TODO - replace with GUI welcome
        self.terminal.printWelcome()
        self.window.full_screen_text(self.welcome_message, title='Welcome to Battleship!')

    def prompt_player_name(self):
        import random
        # TODO - connect with GUI to return real value
        return 'fake player ' + str(random.randint(0, 100))

    def choose_number_of_ships(self):
        # TODO - connect with GUI to prompt user for number of ships 1 to 5
        return 2

    def switch_to_player(self, player):
        # TODO - connect with GUI to prompt to switch to the given player
        return

    def place_ships(self, player):
        if isinstance(player, AIPlayer):
            player.generate_placed_ships()
            return

        # TODO - connect with GUI to prompt player to place their ships
        return

    def choose_if_ai(self):
        # TODO - connect with GUI to prompt user to choose AI or real player
        return True  # true if AI, false if player

    def get_fire_coordinates(self, current_player):
        # TODO - connect with GUI to show current player, opposing player's boards, return coordinates
        return 'A1'

    def show_player_hit(self, current_player):
        # TODO - connect with GUI ti show current player, opposing player's boards, and a successful hit message
        return

    def show_player_miss(self, current_player):
        # TODO - connect with GUI ti show current player, opposing player's boards, and a failed hit message
        return

    def show_player_victory(self, victorious_player):
        # TODO - connect with GUI to show the victory screen, and both player's boards
        return
