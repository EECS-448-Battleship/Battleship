from .Terminal import Terminal
from .AIPlayer import AIPlayer
from .GUI.Window import Window
from .enum import BoardCellState
from .Board import coords_to_loc


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

        for index, ship in enumerate(player.ships):
            player_grid, opponent_grid = self.window.render_board_for_player(player)
            if index == 0:  # 1x1 ships only require a single coordinate
                self.window.show_message('Click a cell on your grid to place the 1x1 ship.')
                row, col = self.window.get_grid_click_event(player_grid)
                loc_str = coords_to_loc(row, col)
                player.place_ship(0, loc_str, loc_str)
            else:  # every other ship requires us to get two valid coordinates
                player_grid, opponent_grid = self.window.render_board_for_player(player)
                self.window.show_message('Click a cell on your grid to place the 1x' + str(index + 1) + ' ship.')
                row_1, col_1 = self.window.get_grid_click_event(player_grid)

                # don't allow the player to select an existing ship as the first coordinate
                done = False
                while not done:
                    loc_str = coords_to_loc(row_1, col_1)
                    if player.board.cell_has_ship(loc_str):
                        row_1, col_1 = self.window.get_grid_click_event(player_grid)
                    else:
                        done = True

                front_loc = coords_to_loc(row_1, col_1)

                # Generate possible other coordinates that don't collide with other ships
                valid_coords = player.board.get_valid_placement_cells_for_ship(row_1, col_1, index + 1)
                overrides = [(x, BoardCellState.Placement) for x in valid_coords]

                # don't allow the player to click a cell that isn't one of the valid placements
                done = False
                while not done:
                    player_grid, opponent_grid = self.window.render_board_for_player(player, overrides)
                    self.window.show_message('Now, click the cell where the other end of the 1x' + str(index + 1) + ' ship should be located.')
                    row_2, col_2 = self.window.get_grid_click_event(player_grid)

                    for coord in valid_coords:
                        if coord[0] == row_2 and coord[1] == col_2:
                            # this is a valid placement, so convert it to a location string and place the ship
                            back_loc = coords_to_loc(row_2, col_2)
                            player.place_ship(index, front_loc, back_loc)
                            done = True
                            break

        # show the player their finalized board before continuing
        self.window.render_board_for_player(player)
        self.window.show_message('Your board has been set up! Click anywhere to continue...')
        self.window.get_click_event()
        return

    def choose_if_ai(self):
        return self.window.two_button_prompt('You can play the game against the computer, or another player.\n \nHow would you like to continue?', yes='Play against computer', no='Add another player')

    def get_fire_coordinates(self, current_player):
        if isinstance(current_player, AIPlayer):
            return current_player.get_fire_coordinates()

        player_grid, opponent_grid = self.window.render_board_for_player(current_player)
        self.window.show_message('Click a cell on ' + current_player.other_player.name + '\'s board to fire a missile.')

        fire_coords = self.window.get_grid_click_event(opponent_grid)
        return coords_to_loc(fire_coords[0], fire_coords[1])

    def show_player_hit(self, current_player):
        # TODO - connect with GUI ti show current player, opposing player's boards, and a successful hit message
        return

    def show_player_miss(self, current_player):
        # TODO - connect with GUI ti show current player, opposing player's boards, and a failed hit message
        return

    def show_player_victory(self, victorious_player):
        # TODO - connect with GUI to show the victory screen, and both player's boards
        return
