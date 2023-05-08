"""
Solves the `Extract the domain name from a URL` codewars kata
url: https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

Instructions:
Write a function that when given a URL as a string, parses out just
the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""


def domain_name(url: str) -> str:
    """Extract the domain name from a URL.

    Parameters
    ----------
    url : str
        A URL as a string.

    Returns
    -------
    str
        The domain name.
    """
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
