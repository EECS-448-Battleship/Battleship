import random
from .Player import Player
from .enum import AIDifficulty
from .Board import convert_loc, coords_to_loc


class AIPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.ai_difficulty = AIDifficulty.Medium

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
            done = False
            while not done:
                # generate a random placement
                front_loc = self.get_random_coord()
                idx = convert_loc(front_loc)
                coords = (idx[0], idx[1])

                # get the valid other locations
                other_locs = self.board.get_valid_placement_cells_for_ship(coords[0], coords[1], index + 1)
                if other_locs is None or len(other_locs) < 1:
                    continue

                # randomly choose one of them
                back_coords = random.choice(other_locs)
                back_loc = coords_to_loc(back_coords[0], back_coords[1])

                self.place_ship(index, front_loc, back_loc)
                done = True

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
        clone = [x for x in self.missile_fire_history]
        clone.reverse()

        for index, record in enumerate(clone):
            if record['successful']:
                return index, record

        return -1, None

    def get_second_strike_coordinates(self, history_record):
        if self.should_try_up(history_record):
            return self.translate_up(history_record['location'])
        elif self.should_try_right(history_record):
            return self.translate_right(history_record['location'])
        elif self.should_try_down(history_record):
            return self.translate_down(history_record['location'])
        elif self.should_try_left(history_record):
            return self.translate_left(history_record['location'])
        else:
            # This shouldn't be possible, but provide a safe value just in case
            return self.get_fire_coordinates_easy()

    def get_fire_coordinates_medium(self):
        last_success_index, last_success_record = self.get_last_successful_fire()
        if last_success_index < 0:
            # we have not hit anything yet, so continue firing
            return self.get_fire_coordinates_easy()

        successful_attempts = [x for x in enumerate(self.missile_fire_history) if x[1]['successful']]

        if len(successful_attempts) < 2:
            # This is the first shot after a successful fire. Start trying the algorithm
            return self.get_second_strike_coordinates(last_success_record)

        direction = self.determine_attempt_direction(successful_attempts)
        if direction is None:
            # This is the first shot after a successful fire. Start trying the algorithm
            return self.get_second_strike_coordinates(last_success_record)

        if direction == 'up':
            # We're in an upward firing pattern
            if self.should_try_up(last_success_record):
                # We can still fire upward
                return self.translate_up(last_success_record['location'])
            else:
                # We were in an upward pattern, but it failed, so let's try a downward pattern from the origin
                origin = self.determine_algorithm_origin(successful_attempts, 'up')
                if self.should_try_down(origin):
                    return self.translate_down(origin['location'])
                else:
                    # Give up
                    return self.get_fire_coordinates_easy()
        elif direction == 'down':
            # We're in a downward firing pattern
            if self.should_try_down(last_success_record):
                # We can still fire downward
                return self.translate_down(last_success_record['location'])
            else:
                # We were in a downward pattern, but it failed, so let's try an upward pattern from the origin
                origin = self.determine_algorithm_origin(successful_attempts, 'down')
                if self.should_try_up(origin):
                    return self.translate_up(origin['location'])
                else:
                    # Give up
                    return self.get_fire_coordinates_easy()
        elif direction == 'left':
            # We're in a leftward firing pattern
            if self.should_try_left(last_success_record):
                # We can still fire leftward
                return self.translate_left(last_success_record['location'])
            else:
                # We were in a leftward pattern, but it failed, so let's try a rightward pattern from the origin
                origin = self.determine_algorithm_origin(successful_attempts, 'left')
                if self.should_try_right(origin):
                    return self.translate_right(origin['location'])
                else:
                    # Give up
                    return self.get_fire_coordinates_easy()
        else:
            # We're in a rightward firing pattern
            if self.should_try_right(last_success_record):
                # We can still fire rightward
                return self.translate_right(last_success_record['location'])
            else:
                # We were in a rightward pattern, but it failed, so let's try a leftward pattern from the origin
                origin = self.determine_algorithm_origin(successful_attempts, 'right')
                if self.should_try_left(origin):
                    return self.translate_left(origin['location'])
                else:
                    # Give up
                    return self.get_fire_coordinates_easy()

    def get_fire_coordinates_hard(self):
        for ship_loc in self.other_player.get_ship_locations():
            if not self.loc_already_attempted(ship_loc):
                return ship_loc

    def get_fire_coordinates(self):
        if self.ai_difficulty == AIDifficulty.Easy:
            return self.get_fire_coordinates_easy()
        elif self.ai_difficulty == AIDifficulty.Medium:
            return self.get_fire_coordinates_medium()
        else:
            return self.get_fire_coordinates_hard()

    def determine_algorithm_origin(self, successful_attempts, direction):
        clone = [x for x in successful_attempts]

        last = clone[0]
        last_row_i, last_col_i = convert_loc(last[1]['location'])

        for index, record in enumerate(clone):
            if index == 0:
                continue

            row_i, col_i = convert_loc(record[1]['location'])
            if direction == 'up' and last_row_i == row_i - 1:
                last = record
                last_col_i = col_i
                last_row_i = row_i
            elif direction == 'down' and last_row_i == row_i + 1:
                last = record
                last_col_i = col_i
                last_row_i = row_i
            elif direction == 'left' and last_col_i == col_i - 1:
                last = record
                last_col_i = col_i
                last_row_i = row_i
            elif direction == 'right' and last_col_i == col_i + 1:
                last = record
                last_col_i = col_i
                last_row_i = row_i
            else:
                return last[1]

        return last[1]

    def determine_attempt_direction(self, successful_attempts):
        last_idx, last_attempt = successful_attempts[-1]
        second_to_idx, second_to_attempt = successful_attempts[-2]

        last_row_i, last_col_i = convert_loc(last_attempt['location'])
        second_row_i, second_col_i = convert_loc(second_to_attempt['location'])

        if second_col_i == last_col_i and last_row_i == (second_row_i + 1):
            return 'down'
        elif second_col_i == last_col_i and last_row_i == (second_row_i - 1):
            return 'up'
        elif second_row_i == last_row_i and last_col_i == (second_col_i + 1):
            return 'right'
        elif second_row_i == last_row_i and last_col_i == (second_col_i - 1):
            return 'left'

    def should_try_up(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[0] > 0 and not self.loc_already_attempted(self.translate_up(history_record['location']))

    def translate_up(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[0] - 1, idx[1])

    def should_try_right(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[1] < 8 and not self.loc_already_attempted(self.translate_right(history_record['location']))

    def translate_right(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[0], idx[1] + 1)

    def should_try_down(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[0] < 8 and not self.loc_already_attempted(self.translate_down(history_record['location']))

    def translate_down(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[0] + 1, idx[1])

    def should_try_left(self, history_record):
        idx = convert_loc(history_record['location'])
        return idx[1] > 0 and not self.loc_already_attempted(self.translate_left(history_record['location']))

    def translate_left(self, loc):
        idx = convert_loc(loc)
        return coords_to_loc(idx[0], idx[1] - 1)
