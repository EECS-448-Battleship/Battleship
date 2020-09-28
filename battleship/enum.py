import enum


class BoardCellState(enum.Enum):
    Empty = 'O'
    Miss = '*'
    Ship = 'S'
    Hit = 'X'
    Unknown = 'U'
