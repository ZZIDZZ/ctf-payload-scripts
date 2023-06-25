from Crypto.Util.number import long_to_bytes
import gmpy2

n = 4155782502547623093831518113976094054382827573251453061239
c = 2669292279100633236493181205299328973407167118230741040683
e = 65537

for i in range(0, 1000000000000):
    root, isExact = gmpy2.iroot(i*n + c, e)
    if isExact:
        print(f"Found root: {i} {long_to_bytes(root)}")
    