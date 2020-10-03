import random
from .Player import Player
from .enum import AIDifficulty


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
        return  # TODO implement this

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
        ship_found = False

        if ship_found == False
            while True:
                rand = self.get_random_coord()
                found = False
                for record in self.missile_fire_history:
                    if record["location"] == rand:
                        found = True
                if not found:
                    return rand
        if ship_found == True

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

    def shoot_top(self):

    def shoot_right(self):

    def shoot_down(self):
        
    def shoot_left(self):

