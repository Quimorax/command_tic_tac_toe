import main
from utilities.matrix_utilities import make_solid_matrix
from utilities.check_utilities import check_game_over

import pytest


def test_rows():
    for player_designation in main.players.values():
        for index in range(main.desk_size):
            matrix = make_solid_matrix(main.desk_size)
            matrix[index] = [player_designation] * main.desk_size
            assert check_game_over(matrix, main.players) is True


def test_columns():
    for player_designation in main.players.values():
        for index in range(main.desk_size):
            matrix = make_solid_matrix(main.desk_size)
            for inner_index in range(main.desk_size):
                matrix[inner_index][index] = player_designation
            assert check_game_over(matrix, main.players) is True


def test_draw():
    matrix = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['O', 'X', 'O']
    ]
    assert check_game_over(matrix, main.players) == 'Draw'


class TestDiagonals:
    def test_left_diagonal(self):
        for player_designation in main.players.values():
            matrix = make_solid_matrix(main.desk_size)
            for index in range(main.desk_size):
                matrix[index][index] = player_designation
            assert check_game_over(matrix, main.players) is True

    def test_right_diagonal(self):
        for player_designation in main.players.values():
            matrix = make_solid_matrix(main.desk_size)
            for index in range(main.desk_size - 1, -1, -1):
                matrix[main.desk_size - index - 1][index] = player_designation
            assert check_game_over(matrix, main.players) is True


if __name__ == '__main__':
    pytest.main()
