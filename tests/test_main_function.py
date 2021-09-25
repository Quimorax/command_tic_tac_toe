import pytest

import main
import utilities

original_make_matrix = utilities.make_matrix
original_make_move = main.make_move
main.set_make_move(lambda matrix, player: None)


class TestDiagonals:
    def test_left_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = [
                [player_designation, None, None],
                [None, player_designation, None],
                [None, None, player_designation]
            ]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_right_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = [
                [None, None, player_designation],
                [None, player_designation, None],
                [player_designation, None, None]
            ]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def teardown(self):
        utilities.set_make_matrix(original_make_matrix)


class TestRows:
    def test_first_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [[player_designation] * 3, [None] * 3, [None] * 3]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_second_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [[None] * 3, [player_designation] * 3, [None] * 3]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_third_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [[None] * 3, [None] * 3, [player_designation] * 3]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message


class TestColumns:
    def test_first_column_win(self):
        for player, player_designation in main.players.items():
            matrix = [
                [player_designation, None, None],
                [player_designation, None, None],
                [player_designation, None, None]
            ]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_second_row_win(self):
        for player, player_designation in main.players.items():
            matrix = [
                [None, player_designation, None],
                [None, player_designation, None],
                [None, player_designation, None]
            ]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message

    def test_third_column_win(self):
        for player, player_designation in main.players.items():
            matrix = [
                [None, None, player_designation],
                [None, None, player_designation],
                [None, None, player_designation]
            ]
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player) == message


def test_with_wrong_player():
    with pytest.raises(NameError):
        utilities.set_make_matrix(
            lambda desk_size: utilities.make_solid_matrix(main.desk_size, placeholder='X')
        )
        main.main('one')


def teardown():
    utilities.set_make_matrix(original_make_matrix)
    main.set_make_move(original_make_move)


if __name__ == '__main__':
    pytest.main()
