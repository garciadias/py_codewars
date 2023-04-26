import pytest

from py_codewars.string_ends_with import solution

FIXED_TESTS_TRUE = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

FIXED_TESTS_FALSE = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)


@pytest.mark.parametrize("text, ending", FIXED_TESTS_TRUE)
def test_solution_true(text, ending):
    assert solution(text, ending) == text.endswith(ending)
