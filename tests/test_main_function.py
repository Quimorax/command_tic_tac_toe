import pytest

import main
import utilities

original_make_matrix = utilities.make_matrix


class TestDiagonals:
    def test_left_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = utilities.make_solid_matrix(main.desk_size)
            for index in range(main.desk_size):
                matrix[index][index] = player_designation
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player, test=True) == message

    def test_right_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = utilities.make_solid_matrix(main.desk_size)
            for index in range(main.desk_size - 1, -1, -1):
                matrix[main.desk_size - index - 1][index] = player_designation
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player, test=True) == message

    def teardown(self):
        utilities.set_make_matrix(original_make_matrix)


def test_rows_wins():
    for player, player_designation in main.players.items():
        for row_index in range(main.desk_size):
            matrix = utilities.make_solid_matrix(main.desk_size)
            matrix[row_index] = [player_designation] * main.desk_size
            utilities.matrix_utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player, test=True) == message


def test_columns_wins():
    for player, player_designation in main.players.items():
        for index in range(main.desk_size):
            matrix = utilities.make_solid_matrix(main.desk_size)
            for inner_index in range(main.desk_size):
                matrix[inner_index][index] = player_designation
            utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            assert main.main(player, test=True) == message


def test_with_wrong_player():
    with pytest.raises(NameError):
        utilities.set_make_matrix(
            lambda desk_size: utilities.make_solid_matrix(main.desk_size, placeholder='X')
        )
        main.main('one')  # if not raise, return 'Draw' because all matrix it's crosses


def teardown():
    utilities.set_make_matrix(original_make_matrix)


if __name__ == '__main__':
    pytest.main()
