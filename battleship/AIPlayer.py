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

    def get_fire_coordinates_easy(self):
        while True:
            rand = self.get_random_coord()
            found = False
            for record in self.missile_fire_history:
                if record["location"] == rand:
                    found = True
            if not found:
                return rand

    def get_fire_coordinates_medium(self):
        
        return 'A1'

    def get_fire_coordinates_hard(self):
        # TODO implement this
        aimbot = self.get_ship_locations()
        for x in aimbot:
            for y in self.missile_fire_history:
                if x != y:
                    return x     

    def get_fire_coordinates(self):
        if self.ai_difficulty == AIDifficulty.Easy:
            return self.get_fire_coordinates_easy()
        elif self.ai_difficulty == AIDifficulty.Medium:
            return self.get_fire_coordinates_medium()
        else:
            return self.get_fire_coordinates_hard()
