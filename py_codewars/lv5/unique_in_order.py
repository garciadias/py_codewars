"""
Solves the `Unique In Order` codewars kata
url: https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

Instructions:
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each
other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""
from typing import Union


def unique_in_order(sequence: Union[str, list, tuple]) -> list:
    """Return a list of items without any elements with the same value next to
    each other and preserving the original order of elements.

    Parameters
    ----------
    sequence : str or list or tuple
        A sequence of elements.

    Returns
    -------
    list
        A list of items without any elements with the same value next to each
        other and preserving the original order of elements.
    """
    sequence = list(sequence)
    if len(sequence) == 0:
        return []
    unique_in_order_list = [sequence[0]]
    for i, item in enumerate(sequence[1:], start=1):
        if item != sequence[i - 1]:
            unique_in_order_list.append(item)
    return unique_in_order_list
