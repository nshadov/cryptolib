#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module containing RollingKey class, implementing
key, that could be used for encryption element by element.

Example:
    rk = RollingKey("ABCD")
    ciphertext = [ chr(ord(c)^ord(k)) for c,k in izip(plaintext,rk) ]
"""

class RollingKey:
    """
     Class implementing rolling key, that could be used
    over and over for encrypting with repeated key.

    WARNING: Rolling codes hould NOT be used for implementations
             where high security is importnant component (like OTP).
    """

    def __init__(self, key):
        self.key = key
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        if self.index >= len(self.key): self.index = 0
        tmp = self.key[self.index]
        self.index += 1
        return tmp

    def __next__(self):
        return self.next()

    def __getitem__(self, index):
        return self.key[index%len(self.key)]

    def __str__(self):
        if len(self.key) > 10:
            return "RollingKey(%s ...)" % self.key[:10]
        else:
            return "RollingKey(%s)" % self.key[:10]

def test():
    rk = RollingKey("ABCD")

    assert rk.next() == "A"
    assert rk.next() == "B"
    assert rk.next() == "C"
    assert rk.next() == "D"
    assert rk.next() == "A"

    assert rk[1000] == "A"

if __name__ == "__main__":
    test()
