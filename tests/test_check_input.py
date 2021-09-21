import unittest
import main
from utilities.matrix_utilities import make_matrix
from utilities.check_utilities import check_input


class TestCheckInput(unittest.TestCase):
    matrix = make_matrix(main.desk_size)

    def test_input_too_large_coordinate(self):
        with self.assertRaises(ValueError) as error:
            check_input(main.desk_size ** 2 + 1, TestCheckInput.matrix)
        self.assertEqual('Too large coordinate', error.exception.args[0])

    def test_input_too_small_coordinate(self):
        with self.assertRaises(ValueError) as error:
            check_input(0, TestCheckInput.matrix)
        self.assertEqual('Too small coordinate', error.exception.args[0])

    def test_not_available_coordinate(self):
        matrix = TestCheckInput.matrix.copy()
        matrix[0][0] = main.players['cross']
        with self.assertRaises(ValueError) as error:
            check_input(1, matrix)
        self.assertEqual('Coordinate is already occupied', error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
