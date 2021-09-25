import pytest

import main
from utilities import check_input
from utilities import make_matrix

matrix = make_matrix(main.desk_size)


def test_input_too_large_coordinate():
    with pytest.raises(ValueError) as error:
        check_input(main.desk_size ** 2 + 1, matrix)
    assert 'Too large coordinate' == error.value.args[0]


def test_input_too_small_coordinate():
    with pytest.raises(ValueError) as error:
        check_input(0, matrix)
    assert 'Too small coordinate' == error.value.args[0]


def test_not_available_coordinate():
    global matrix
    matrix = matrix.copy()
    matrix[0][0] = main.players['cross']
    with pytest.raises(ValueError) as error:
        check_input(1, matrix)
    assert 'Coordinate is already occupied' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
