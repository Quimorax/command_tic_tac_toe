import pytest

import main
import tests.support_tools as support_tools
import utilities

original_make_matrix = utilities.make_matrix
original_make_move = main.make_move
support_tools.set_make_move(lambda matrix, player: None)


class TestDiagonals:
    def test_left_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = [
                [player_designation, None, None],
                [None, player_designation, None],
                [None, None, player_designation]
            ]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_right_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = [
                [None, None, player_designation],
                [None, player_designation, None],
                [player_designation, None, None]
            ]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def teardown(self):
        support_tools.set_make_matrix(original_make_matrix)


class TestRows:
    def test_first_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [[player_designation] * 3, [None] * 3, [None] * 3]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_second_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [[None] * 3, [player_designation] * 3, [None] * 3]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_third_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [[None] * 3, [None] * 3, [player_designation] * 3]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def teardown(self):
        support_tools.set_make_matrix(original_make_matrix)


class TestColumns:
    def test_first_column_win(self):
        for player, player_designation in main.players.items():
            matrix = [
                [player_designation, None, None],
                [player_designation, None, None],
                [player_designation, None, None]
            ]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_second_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [
                [None, player_designation, None],
                [None, player_designation, None],
                [None, player_designation, None]
            ]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_third_column_win(self):
        for player, player_designation in main.players.items():
            matrix = [
                [None, None, player_designation],
                [None, None, player_designation],
                [None, None, player_designation]
            ]
            support_tools.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def teardown(self):
        support_tools.set_make_matrix(original_make_matrix)


def test_with_wrong_player():
    with pytest.raises(NameError):
        support_tools.set_make_matrix(
            lambda desk_size: support_tools.make_solid_matrix(main.desk_size, placeholder='X')
        )
        main.main('one')


def teardown():
    support_tools.set_make_matrix(original_make_matrix)
    support_tools.set_make_move(original_make_move)


if __name__ == '__main__':
    pytest.main()
