from termcolor import colored


def pretty_matrix_print(matrix: list[list], bracket_color='white', separator_color='white') -> None:
    """Pretty matrix print with color instead of GUI."""
    for list_of_items in matrix:
        left_bracket, right_bracket = colored('[', bracket_color), colored(']', bracket_color)
        separator = colored(", ", separator_color)
        items = separator.join(str(item) for item in list_of_items)
        print(f"{left_bracket}{items}{right_bracket}")


def make_matrix(desk_size: int) -> list[list[int]]:
    """Make matrix (size: desk_size ** 2) with coordinates 1 — desk_size ** 2 (including)."""
    matrix = []
    digits_iterator = iter(range(1, desk_size ** 2 + 1))
    for _ in range(desk_size):
        matrix.append([next(digits_iterator) for _ in range(desk_size)])
    return matrix
