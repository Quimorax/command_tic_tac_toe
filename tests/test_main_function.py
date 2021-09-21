import unittest
import main
from utilities import matrix_utilities

original_make_matrix = matrix_utilities.make_matrix


class TestMainFunction(unittest.TestCase):
    """All tests test two players"""

    def test_rows_wins(self):
        for player, player_designation in main.players.items():
            for row_index in range(main.desk_size):
                matrix = matrix_utilities.make_solid_matrix(main.desk_size)
                matrix[row_index] = [player_designation] * main.desk_size
                matrix_utilities.set_make_matrix(lambda desk_size: matrix)
                message = f'Player {main.colored(player, main.players_colors[player])} win'
                self.assertEqual(main.main(player, test=True), message)
        matrix_utilities.set_make_matrix(original_make_matrix)

    def test_columns_wins(self):
        for player, player_designation in main.players.items():
            for index in range(main.desk_size):
                matrix = matrix_utilities.make_solid_matrix(main.desk_size)
                for inner_index in range(main.desk_size):
                    matrix[inner_index][index] = player_designation
                matrix_utilities.set_make_matrix(lambda desk_size: matrix)
                message = f'Player {main.colored(player, main.players_colors[player])} win'
                self.assertEqual(main.main(player, test=True), message)
        matrix_utilities.set_make_matrix(original_make_matrix)

    def test_left_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = matrix_utilities.make_solid_matrix(main.desk_size)
            for index in range(main.desk_size):
                matrix[index][index] = player_designation
            matrix_utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            self.assertEqual(main.main(player, test=True), message)
        matrix_utilities.set_make_matrix(original_make_matrix)

    def test_right_diagonal_wins(self):
        for player, player_designation in main.players.items():
            matrix = matrix_utilities.make_solid_matrix(main.desk_size)
            for index in range(main.desk_size - 1, -1, -1):
                matrix[main.desk_size - index - 1][index] = player_designation
            matrix_utilities.set_make_matrix(lambda desk_size: matrix)
            message = f'Player {main.colored(player, main.players_colors[player])} win'
            self.assertEqual(main.main(player, test=True), message)
        matrix_utilities.set_make_matrix(original_make_matrix)

    def test_with_wrong_player(self):
        with self.assertRaises(NameError):
            matrix_utilities.set_make_matrix(
                lambda desk_size: matrix_utilities.make_solid_matrix(main.desk_size, placeholder='X')
            )
            main.main('one')  # if not raise, return 'Draw' because all matrix it's crosses
        matrix_utilities.set_make_matrix(original_make_matrix)


if __name__ == '__main__':
    unittest.main()
