from .Terminal import Terminal


class GameEvents:
    terminal = Terminal()

    def show_welcome(self):
        # TODO - replace with GUI welcome
        self.terminal.printWelcome()

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
        # TODO - connect with GUI to prompt player to place their ships
        return

    def choose_if_ai(self):
        # TODO - connect with GUI to prompt user to choose AI or real player
        return True  # true if AI, false if player
