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

    def get_fire_coordinates_easy(self):
        # TODO implement this
        return 'A1'

    def get_fire_coordinates_medium(self):
        # TODO implement this
        return 'A1'

    def get_fire_coordinates_hard(self):
        # TODO implement this
        return 'A1'

    def get_fire_coordinates(self):
        if self.ai_difficulty == AIDifficulty.Easy:
            return self.get_fire_coordinates_easy()
        elif self.ai_difficulty == AIDifficulty.Medium:
            return self.get_fire_coordinates_medium()
        else:
            return self.get_fire_coordinates_hard()
