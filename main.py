"""Command version of tic-tac-toe with pretty colored print."""

__version__ = '1.0.0'

import argparse
from random import choice
from typing import Optional, Callable

from colorama import init
from termcolor import colored

import utilities

init()  # for Windows support

players_colors = {'cross': 'red', 'zero': 'green'}
players = {'cross': colored('X', players_colors['cross']), 'zero': colored('O', players_colors['zero'])}


def create_parser() -> argparse.ArgumentParser:
    """Create parser that processes command-line parameters."""
    parser = argparse.ArgumentParser(
        prog='tic-tac-toe',
        description="""It's command version of tic-tac-toe with colored pretty print instead of GUI.""",
        epilog=f"""tic-tac-toe {__version__} - (C) September 2021 Quimorax"""  # some fun :)
    )
    parser.add_argument('-p', '--player', default=choice(tuple(players)),
                        help="Determines which player will go first (default chose random)")
    parser.add_argument('-ds', '--desk-size', default=3, type=int, help="Determines desk size (default 3)")
    return parser


def make_move(matrix: list[list], player: str) -> None:
    """Changes the index of the matrix to the entered coordinate (if no exceptions).

    Args:
        matrix: matrix with coordinates and optionally players.
        player: means "cross" or "zero".

    Notes:
        Function has an infinite cycle that ends only after valid input.

    """
    while True:
        try:
            step_coordinate = int(input('Enter coordinate: '))
            utilities.check_input(step_coordinate, matrix)
        except ValueError as error:
            print(f'{error}, enter one more time...')
        else:
            value = [elem for elem in matrix if step_coordinate in elem][0]
            matrix[matrix.index(value)][value.index(step_coordinate)] = players[player]
            break


def set_make_move(function: Callable) -> None:
    """Set "make_move" for easy testing in unittests."""
    global make_move
    make_move = function


def main(player_making_first_move: Optional[str]) -> str:
    """Main function that runs the project.

    Args:
        player_making_first_move: Player who making first move. Only can be "cross" or "zero".

    Returns:
        Return colored 'Draw' or message about who won.

    Raises:
        NameError: if player_making_first_move not "cross" or "zero".

    """
    if player_making_first_move not in players:
        raise NameError('Player only can be "cross" or "zero"')
    matrix = utilities.matrix_utilities.make_matrix(desk_size)
    utilities.pretty_matrix_print(matrix)
    player = player_making_first_move
    while True:
        print(f'Player {colored(player, players_colors[player])} makes a move')
        make_move(matrix, player)
        utilities.pretty_matrix_print(matrix)
        value = utilities.check_game_conditions(matrix, players)
        if value == utilities.results_according_conditions.DRAW:
            return colored(value, 'yellow')
        elif value == utilities.results_according_conditions.WIN:
            return f'Player {colored(player, players_colors[player])} win'
        else:  # if value is "Continue..."
            player = get_next_player(player)


def get_next_player(available_player: str) -> str:
    return 'cross' if available_player == 'zero' else 'zero'


parser = create_parser()
namespace = parser.parse_args()
desk_size = namespace.desk_size

if __name__ == '__main__':
    print(main(namespace.player))
