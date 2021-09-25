import pytest

import main
from utilities import make_matrix


def test_last_coordinate():
    last_step_coordinate = main.desk_size ** 2
    for player in main.players:
        matrix = make_matrix(main.desk_size)
        main.input = lambda message: last_step_coordinate
        main.make_move(matrix, player)
        assert all(last_step_coordinate not in list_ for list_ in matrix) is True


def test_third_coordinate():
    third_step_coordinate = main.desk_size  # because matrix size desk_size ** 2
    for player in main.players:
        matrix = make_matrix(main.desk_size)
        main.input = lambda message: third_step_coordinate
        main.make_move(matrix, player)
        assert all(third_step_coordinate not in list_ for list_ in matrix) is True


def test_first_coordinate():
    first_step_coordinate = 1
    for player, player_designation in main.players.items():
        matrix = make_matrix(main.desk_size)
        main.input = lambda message: first_step_coordinate
        main.make_move(matrix, player)
        assert all(first_step_coordinate not in list_ for list_ in matrix) is True


def teardown():
    main.input = input


if __name__ == '__main__':
    pytest.main()
