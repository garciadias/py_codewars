from py_codewars.lv5.unique_in_order import unique_in_order


def test_unique_in_order_str():
    """Test unique_in_order on a string."""
    assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]
    assert unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"]


def test_unique_in_order_list():
    """Test unique_in_order on a list."""
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]


def test_unique_in_order_tuple():
    """Test unique_in_order on a tuple."""
    assert unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3]


def test_unique_in_order_empty():
    """Test unique_in_order on an empty sequence."""
    assert unique_in_order("") == []
    assert unique_in_order([]) == []
    assert unique_in_order(()) == []
