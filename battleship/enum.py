import enum


class BoardCellState(enum.Enum):
    Empty = 'O'
    Miss = '*'
    Ship = 'S'
    Hit = 'X'
    Unknown = 'U'


class AIDifficulty(enum.Enum):
    Easy = 'easy'
    Medium = 'medium'
    Hard = 'hard'
