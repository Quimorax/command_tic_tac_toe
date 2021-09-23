from typing import Union, Callable, Any

from termcolor import colored


def pretty_matrix_print(matrix: list[list[Union[str, int]]], bracket_color='white', separator_color='white') -> None:
    """Pretty matrix print with color instead of GUI."""
    for list_of_items in matrix:
        left_bracket, right_bracket = colored('[', bracket_color), colored(']', bracket_color)
        separator = colored(", ", separator_color)
        items = separator.join(str(elem) for elem in list_of_items)
        print(f"{left_bracket}{items}{right_bracket}")


def make_matrix(desk_size) -> list[list[int]]:
    """Make matrix (size: desk_size ** 2) with coordinates 1 — desk_size ** 2 (including)."""
    matrix = []
    digits_iterator = iter(range(1, desk_size ** 2 + 1))
    for _ in range(desk_size):
        matrix.append([next(digits_iterator) for _ in range(desk_size)])
    return matrix


def make_solid_matrix(desk_size, *, placeholder=...) -> list[list[Any]]:
    """Make a solid matrix, which used in unittests."""
    return [[placeholder for _ in range(desk_size)] for _ in range(desk_size)]


def set_make_matrix(function: Callable) -> None:
    """Set "make_matrix" for easy testing in unittests."""
    global make_matrix
    make_matrix = function
