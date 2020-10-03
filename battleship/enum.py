import enum


class BoardCellState(enum.Enum):
    Empty = 'O'
    Miss = '*'
    Ship = 'S'
    Hit = 'X'
    Unknown = 'U'


def board_cell_state_to_render_color(state):
    if not isinstance(state, BoardCellState):
        return 255, 0, 0
    elif state == BoardCellState.Empty:
        return 51, 108, 167
    elif state == BoardCellState.Miss:
        return 247, 159, 159
    elif state == BoardCellState.Ship:
        return 90, 90, 90
    elif state == BoardCellState.Hit:
        return 255, 0, 0
    else:
        return 0, 0, 0


class AIDifficulty(enum.Enum):
    Easy = 'easy'
    Medium = 'medium'
    Hard = 'hard'
