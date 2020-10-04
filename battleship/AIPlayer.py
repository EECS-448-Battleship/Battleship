import random
from .Player import Player
from .enum import AIDifficulty
from .Board import convert_loc, coords_to_loc


class AIPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.ai_difficulty = AIDifficulty.Easy

    def set_difficulty(self, difficulty):
        if not isinstance(difficulty, AIDifficulty):
            raise Exception('Invalid difficulty! Must be an AIDifficulty.')

        self.ai_difficulty = difficulty

    def get_random_coord(self):
        """Get a random co-ordinate on the grid in the form of a location string (e.g. "A1" or "D8")
        """
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return str(random.choice(cols)) + str(random.choice(rows))

    def generate_placed_ships(self):
        for index, ship in enumerate(self.ships):
            # generate a random placement
            front_loc = self.get_random_coord()
            idx = convert_loc(front_loc)
            coords = (idx[0], idx[1])

            # get the valid other locations
            other_locs = self.board.get_valid_placement_cells_for_ship(coords[0], coords[1], index + 1)

            # randomly choose one of them
            back_coords = random.choice(other_locs)
            back_loc = coords_to_loc(back_coords[0], back_coords[1])

            self.place_ship(index, front_loc, back_loc)

    def loc_already_attempted(self, loc):
        for record in self.missile_fire_history:
            if record['location'] == loc:
                return True
        return False

    def get_fire_coordinates_easy(self):
        while True:
            rand = self.get_random_coord()
            if not self.loc_already_attempted(rand):
                return rand

    def get_last_successful_fire(self):
        for index, record in enumerate(self.missile_fire_history):
            if record['successful']:
                return index, record

        return -1, None

    def get_fire_coordinates_medium(self):
        last_success_index, last_success_record = self.get_last_successful_fire()
        if last_success_index < 0:
            # we have not hit anything yet, so continue firing
            return self.get_fire_coordinates_easy()

        # We've hit at least one ship successfully
        last_success_and_later = self.missile_fire_history[last_success_index:]

        # Order of attempts: translate up, right, down, left

        if len(last_success_and_later) < 2:
            # This is the first shot after a successful fire. Start trying the algorithm
            if self.should_try_up(last_success_record):
                return self.translate_up(last_success_record['location'])
            elif self.should_try_right(last_success_record):
                return self.translate_right(last_success_record['location'])
            elif self.should_try_down(last_success_record):
                return self.translate_down(last_success_record['location'])
            elif self.should_try_left(last_success_record):
                return self.translate_left(last_success_record['location'])
            else:
                # This shouldn't be possible, but provide a safe value just in case
                return self.get_fire_coordinates_easy()

    def get_fire_coordinates_hard(self):
        for ship_loc in self.get_ship_locations():
            if not self.loc_already_attempted(ship_loc):
                return ship_loc

    def get_fire_coordinates(self):
        if self.ai_difficulty == AIDifficulty.Easy:
            return self.get_fire_coordinates_easy()
        elif self.ai_difficulty == AIDifficulty.Medium:
            return self.get_fire_coordinates_medium()
        else:
            return self.get_fire_coordinates_hard()

    def should_try_up(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[1] > 0

    def translate_up(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[1] - 1, idx[0])

    def should_try_right(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[0] < 8

    def translate_right(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[1], idx[0] + 1)

    def should_try_down(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[1] < 8

    def translate_down(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[1] + 1, idx[0])

    def should_try_left(self, loc):
        idx = convert_loc(loc)
        return idx[0] > 0

    def translate_left(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[1], idx[0] - 1)
