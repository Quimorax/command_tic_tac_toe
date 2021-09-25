from typing import Union


def check_game_over(matrix: list[list[Union[str, int]]], players: dict) -> Union[str, bool]:
    """Check game over conditions.

    Returns:
        "Draw" for situations when check segments no return True and all desk type elements str.
        True if game over conditions are completed.
        False if none of the above are completed.

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
                return True
    if all(type(elem) == str for list_ in matrix for elem in list_):
        return 'Draw'
    return False


def check_input(step_coordinate: int, matrix: list[list[Union[str, int]]]) -> None:
    """Check input coordinate.

    Raises:
        ValueError: if coordinate too small, too large or occupied

    """
    if step_coordinate < 1:  # 1: min available coordinate
        raise ValueError('Too small coordinate')
    if step_coordinate > len(matrix) ** 2:  # desk_size ** 2: max available coordinate
        raise ValueError('Too large coordinate')
    if not [step_coordinate for list_ in matrix if step_coordinate in list_]:
        raise ValueError('Coordinate is already occupied')
