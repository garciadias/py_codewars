"""
Soving the following codewars kata:
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

Instructions:
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(text: str, ending: str) -> bool:
    """Return True if text ends with ending, else False.

    Parameters
    ----------
    text : str
        The string to check.
    ending : str
        The string to check if it is at the end of text.

    Returns
    -------
    bool:
        True if text ends with ending, else False.
    """
    return text.endswith(ending)
