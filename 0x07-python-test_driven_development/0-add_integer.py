#!/usr/bin/python3
"""Defines a function to add integers."""


def add_integer(a, b=98):
    """Return the integer result addition of a and b.

    Typecast float arguements to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
