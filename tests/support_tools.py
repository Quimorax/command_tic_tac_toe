"""Contain support tools for pytests."""

from typing import Callable, Any

import main
import utilities


def make_solid_matrix(desk_size: int, *, placeholder=None) -> list[list[Any]]:
    """Make a solid matrix with some placeholder."""
    return [[placeholder for _ in range(desk_size)] for _ in range(desk_size)]


def set_make_matrix(function: Callable) -> None:
    """Set "make_matrix" for easy testing in pytests."""
    utilities.make_matrix = function


def set_make_move(function: Callable) -> None:
    """Set "make_move" for easy testing in pytests."""
    main.make_move = function
