"""
Solves the `Moving Zeros To The End` codewars kata
url: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Instructions:
Write an algorithm that takes an array and moves all of the zeros
to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst: list) -> list:
    """Move all of the zeros to the end, preserving the order of the other
    elements.

    Parameters
    ----------
    lst : list
        A list of integers.

    Returns
    -------
    list
        A list of integers with all of the zeros moved to the end, preserving
        the order of the other elements.
    """
    new_list = [item for item in lst if item is False or item != 0]
    new_list.extend([0] * (len(lst) - len(new_list)))
    return new_list
