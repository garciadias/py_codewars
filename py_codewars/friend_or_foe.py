"""
Solving Friend or Foe Kata
url: https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

Instructions:
Make a program that filters a list of strings and returns a list with only
your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a
friend of yours! Otherwise,  you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
"""


def friend(x: list[str]) -> list[str]:
    """Return a list of friends from a list of names.
    Names with exactly 4 letters are considered friends.

    Parameters
    ----------
    x : list
        A list of names.

    Returns
    -------
    list:
        A list of names that are exactly 4 letters long.
    """
    return [name for name in x if len(name) == 4]
