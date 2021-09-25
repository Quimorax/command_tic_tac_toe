import pytest

import main
from utilities import check_game_conditions, results_according_conditions, make_matrix


class TestRows:
    def test_first_row(self):
        for player_designation in main.players.values():
            matrix = [[player_designation] * 3, [None] * 3, [None] * 3]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN

    def test_second_row(self):
        for player_designation in main.players.values():
            matrix = [[None] * 3, [player_designation] * 3, [None] * 3]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN

    def test_third_row(self):
        for player_designation in main.players.values():
            matrix = [[None] * 3, [None] * 3, [player_designation] * 3]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN


class TestColumns:
    def test_first_column(self):
        for player_designation in main.players.values():
            matrix = [
                [player_designation, None, None],
                [player_designation, None, None],
                [player_designation, None, None]
            ]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN

    def test_second_column(self):
        for player_designation in main.players.values():
            matrix = [
                [None, player_designation, None],
                [None, player_designation, None],
                [None, player_designation, None]
            ]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN

    def test_third_column(self):
        for player_designation in main.players.values():
            matrix = [
                [None, None, player_designation],
                [None, None, player_designation],
                [None, None, player_designation]
            ]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN


class TestDiagonals:
    def test_left_diagonal(self):
        for player_designation in main.players.values():
            matrix = [
                [player_designation, None, None],
                [None, player_designation, None],
                [None, None, player_designation]
            ]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN

    def test_right_diagonal(self):
        for player_designation in main.players.values():
            matrix = [
                [None, None, player_designation],
                [None, player_designation, None],
                [player_designation, None, None]
            ]
            assert check_game_conditions(matrix, main.players) == results_according_conditions.WIN


def test_draw():
    matrix = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['O', 'X', 'O']
    ]
    assert check_game_conditions(matrix, main.players) == results_according_conditions.DRAW


def test_continue():
    matrix = make_matrix(3)
    assert check_game_conditions(matrix, main.players) == results_according_conditions.CONTINUE


if __name__ == '__main__':
    pytest.main()
