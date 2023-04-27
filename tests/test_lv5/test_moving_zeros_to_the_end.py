from py_codewars.lv5.moving_zeros_to_the_end import move_zeros


def test_move_zeros():
    lst_input = [1, 0, 1, 2, 0, 1, 3]
    lst_output = [1, 1, 2, 1, 3, 0, 0]
    assert move_zeros(lst_input) == lst_output


def test_move_zeros_with_bool():
    lst_input = [False, 1, 0, 1, 2, 0, 1, 3]
    lst_output = [False, 1, 1, 2, 1, 3, 0, 0]
    assert move_zeros(lst_input) == lst_output


def test_move_zeros_with_mixed_types():
    lst_input = ["a", "b", None, "c", "d", False, 0.0, 1, 2, 0, 1, 3, True, 1]
    lst_output = ["a", "b", None, "c", "d", False, 1, 2, 1, 3, True, 1, 0, 0]
    assert move_zeros(lst_input) == lst_output
