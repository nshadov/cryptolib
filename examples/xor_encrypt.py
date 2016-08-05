#!/usr/bin/env python

import sys
sys.path.append("../../")
from itertools import izip

from cryptolib import RollingKey, cryptolib as cl

key = "1a ff e7 bc d0 19"
plaintext = "The quick brown fox"

rk = RollingKey(cl.hexstr2int(key))
print [chr(ord(c)^k) for c,k in izip(plaintext,rk)]

