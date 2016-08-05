#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Basic primitives for cryptography and cryptoanalysis tools.
"""

from itertools import izip



def pairwise(iterable):
    """
    Converts string to list of pairs of consecutive symbol pairs.

    example:
      "The quick brown fox" => ['Th', 'e ', 'qu', 'ic', 'k ', 'br', 'ow', 'n ', 'fo'] )
    """
    it = iter(iterable)
    pairs = izip(it, it)
    return ["%s%s" % (x[0], x[1]) for x in pairs]

def str2int(plaintext):
    """
    Converts string (plaintext) to list of integers.

    example:
      "abcd" => [65, 66, 67, 68]
    """
    return [ord(c) for c in plaintext]

def hexstr2int(hexstr):
    """
    Convert string of hex values to list of integers.

    example:
      "1a 1b 1c 1d" => [26, 27, 28, 29]
    """
    return [int(x, 16) for x in pairwise(hexstr.replace(" ", ""))]


def test():
    "Tests for primitives"

    import RollingKey

    plaintext = "The quick brown fox"
    key = "1a 1b 1c 1d"
    rk = RollingKey(key)

    assert pairwise(plaintext) == ['Th', 'e ', 'qu', 'ic', 'k ', 'br', 'ow', 'n ', 'fo']
    assert hexstr2int(key) == [26, 27, 28, 29]
    assert str2int("ABCD") == [65, 66, 67, 68]

if __name__ == "__main__":
    test()
