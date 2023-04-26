import pytest

from py_codewars.string_ends_with import solution

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)


@pytest.mark.parametrize("text, ending", fixed_tests_True)
def test_solution_True(text, ending):
    assert solution(text, ending) == text.endswith(ending)
