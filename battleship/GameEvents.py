from .Terminal import Terminal
from .AIPlayer import AIPlayer
from .GUI.Window import Window


class GameEvents:
    terminal = Terminal()
    window = Window()

    welcome_message = '\n \n'.join([
        'You will get started by choosing the number of ships you want to play with.',
    ])

    def show_welcome(self):
        self.terminal.printWelcome()
        self.window.full_screen_text(self.welcome_message, title='Welcome to Battleship!')

    def prompt_player_name(self):
        return self.window.get_input('Enter player name:')

    def choose_number_of_ships(self):
        first = True
        while True:
            text = 'Enter number of ships to play with (1 to 5)'
            if not first:
                text += '. (Invalid. Please try again.)'
            else:
                text += ':'

            input = self.window.get_input(text)

            if first:
                first = False

            try:
                input_int = int(input)
                if 6 > input_int > 0:
                    return input_int
            except:
                pass

    def switch_to_player(self, player):
        if isinstance(player, AIPlayer):
            self.window.full_screen_text('It is now the computer\'s turn.', title='Switch Players')
            return

        self.window.full_screen_text('It is now ' + str(player.name) + '\'s turn. Switch players before the board is revealed.', title='Switch Players')
        return

    def place_ships(self, player):
        if isinstance(player, AIPlayer):
            player.generate_placed_ships()
            return

        generated_ships = []
        for index, ship in enumerate(player.ships):
            player_grid, opponent_grid = self.window.render_board_for_player(player)
            if index == 0:
                self.window.show_message('Click a cell on your grid to place the 1x1 ship.')
                row, col = self.window.get_grid_click_event(player_grid)
                print((row, col))
            else:
                player_grid, opponent_grid = self.window.render_board_for_player(player)
                self.window.show_message('Click a cell on your grid to place the 1x' + str(index + 1) + ' ship.')
                row_1, col_1 = self.window.get_grid_click_event(player_grid)

                # Generate possible other coordinates - TODO move to Board class
                valid_coords = []
                ship_length_offset = index

                # Vertical upward
                if row_1 - ship_length_offset >= 0:
                    valid_coords.append((row_1 - ship_length_offset, col_1))

                # Vertical downward
                if row_1 + ship_length_offset < 9:
                    valid_coords.append((row_1 + ship_length_offset, col_1))

                # Horizontal leftward
                if col_1 - ship_length_offset >= 0:
                    valid_coords.append((row_1, col_1 - ship_length_offset))

                # Horizontal rightward
                if col_1 + ship_length_offset < 9:
                    valid_coords.append((row_1, col_1 + ship_length_offset))

                done = False
                while not done:
                    player_grid, opponent_grid = self.window.render_board_for_player(player)
                    self.window.show_message('Now, click the cell where the other end of the 1x' + str(index + 1) + ' ship should be located.')
                    row_2, col_2 = self.window.get_grid_click_event(player_grid)

                    for coord in valid_coords:
                        if coord[0] == row_2 and coord[1] == col_2:
                            print(coord)
                            # TODO convert coordinate to loc string and call player.place_ship for the index
                            done = True
                            break



        # TODO - connect with GUI to prompt player to place their ships
        self.window.render_board_for_player(player)
        return

    def choose_if_ai(self):
        return self.window.two_button_prompt('You can play the game against the computer, or another player.\n \nHow would you like to continue?', yes='Play against computer', no='Add another player')

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
