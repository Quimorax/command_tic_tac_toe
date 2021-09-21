import unittest
import main
from utilities.matrix_utilities import make_matrix


class TestMakeMove(unittest.TestCase):
    """All tests test two player names"""

    def test_last_coordinate(self):
        last_step_coordinate = main.desk_size ** 2
        for player in main.players:
            matrix = make_matrix(main.desk_size)
            print(player)
            print(f'Enter this: {last_step_coordinate}')
            main.make_move(matrix, player)
            self.assertEqual(all(last_step_coordinate not in list_ for list_ in matrix), True)

    def test_third_coordinate(self):
        third_step_coordinate = main.desk_size  # because matrix size desk_size ** 2
        for player in main.players:
            matrix = make_matrix(main.desk_size)
            print(player)
            print(f'Enter this: {third_step_coordinate}')
            main.make_move(matrix, player)
            self.assertEqual(all(third_step_coordinate not in list_ for list_ in matrix), True)

    def test_first_coordinate(self):
        first_step_coordinate = 1
        for player, player_designation in main.players.items():
            matrix = make_matrix(main.desk_size)
            print(player)
            print(f'Enter this: {first_step_coordinate}')
            main.make_move(matrix, player)
            self.assertEqual(all(first_step_coordinate not in list_ for list_ in matrix), True)


if __name__ == '__main__':
    unittest.main()
