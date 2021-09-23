"""Command version of tic-tac-toe with pretty colored print."""

__version__ = '1.0.0'

import argparse
from random import choice
from typing import Optional, Union

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


parser = create_parser()
namespace = parser.parse_args()
desk_size = namespace.desk_size


def make_move(matrix: list[list[Union[str, int]]], player) -> None:
    """Changes the index of the matrix to the entered coordinate (if no exceptions).

    Args:
        matrix: matrix with coordinates and optionally players.
        player: means "cross" or "zero".

    """
    while True:
        try:
            step_coordinate = int(input('Enter coordinate: '))
            utilities.check_utilities.check_input(step_coordinate, matrix)
        except ValueError as error:
            print(f'{error}, enter one more time..')
        else:
            value = [elem for elem in matrix if step_coordinate in elem][0]
            matrix[matrix.index(value)][value.index(step_coordinate)] = players[player]
            break


def main(player_making_first_move: Optional[str], *, test=False) -> str:
    """Main function that runs the project.

    Args:
        player_making_first_move: Only can be "cross" or "zero". If player_making_first_move is None,
            chosen random in function "create_parser".
        test: Need for testing in unittests because the output will not be taken, because for the comfort of
            testing (so as not to enter many values), the matrix creation function will be changed.

    Returns:
        Colored 'Draw' if value (check_game_over result) return 'Draw' or message about who won.

    Raises:
        NameError: if player_making_first_move not "cross" or "zero".

    """
    if player_making_first_move not in players:
        raise NameError('Player only can be "cross" or "zero"')
    matrix = utilities.matrix_utilities.make_matrix(desk_size)
    utilities.matrix_utilities.pretty_matrix_print(matrix)
    player = player_making_first_move
    while True:
        value = utilities.check_utilities.check_game_over(matrix, players)
        if not value:
            print(f'Player {colored(player, players_colors[player])} makes a move')
            make_move(matrix, player)
            utilities.matrix_utilities.pretty_matrix_print(matrix)
            player = get_next_player(player)
        elif value == 'Draw':
            return colored(value, 'yellow')
        else:  # if value
            if not test:
                player = get_next_player(player)
            return f'Player {colored(player, players_colors[player])} win'


def get_next_player(available_player: str) -> str:
    return 'cross' if available_player == 'zero' else 'zero'


if __name__ == '__main__':
    print(main(namespace.player))
