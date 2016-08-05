# CryptoLib

## Description

CryptLib is small collection of essential cryptography primitives for cryptography and cryptoanalysis.

## Install

```
git clone https://github.com/nshadov/cryptolib.git
```

## Example Usage

Encrypting string with XOR cipher using static rolling key:

```
import sys
sys.path.append("../../")
from itertools import izip

from cryptolib import RollingKey, cryptolib as cl

key = "1a ff e7 bc d0 19"
plaintext = "The quick brown fox"

rk = RollingKey(cl.hexstr2int(key))
print [chr(ord(c)^k) for c,k in izip(plaintext,rk)]
```

## Bugs & Credits

Please submit bugs/propositions via GitHub.

Author: nshadov