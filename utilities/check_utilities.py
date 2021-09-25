from collections import namedtuple


_Results = namedtuple('Results', ['CONTINUE', 'DRAW', 'WIN'])
results_according_conditions = _Results('Continue...', 'Draw', 'Win')


def check_game_conditions(matrix: list[list], players: dict) -> str:
    """Check game conditions.

    Returns:
        "Win" If the player has completely filled a row, diagonal or column.
        "Draw" for situations when check segments no return "Win" and all desk only contains players (str).
        "Continue" if none of the above are completed.

    """
    win_variants = ([players['cross']] * len(matrix), [players['zero']] * len(matrix))
    matrix_segments = {
        'rows': matrix, 'columns': (list(column) for column in zip(*matrix)),
        'diagonals': (
            [matrix[i][i] for i in range(len(matrix))],
            [matrix[len(matrix) - i - 1][i] for i in range(len(matrix) - 1, -1, -1)]
        )
    }
    for segments in matrix_segments.values():
        for segment in segments:
            if segment in win_variants:
                return results_according_conditions.WIN
    if all(type(elem) == str for list_ in matrix for elem in list_):
        return results_according_conditions.DRAW
    return results_according_conditions.CONTINUE


def check_input(step_coordinate: int, matrix: list[list]) -> None:
    """Check input coordinate.

    Raises:
        ValueError: if coordinate too small, too large or occupied.

    """
    if step_coordinate < 1:  # 1: min available coordinate
        raise ValueError('Too small coordinate')
    if step_coordinate > len(matrix) ** 2:  # desk_size ** 2: max available coordinate
        raise ValueError('Too large coordinate')
    if not [step_coordinate for list_ in matrix if step_coordinate in list_]:
        raise ValueError('Coordinate is already occupied')
