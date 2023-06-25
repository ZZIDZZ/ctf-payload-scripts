import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long

n = 4155782502547623093831518113976094054382827573251453061239
e = 65537
c = 2669292279100633236493181205299328973407167118230741040683
# use msieve, yafu or factordb to factor small n
p = 63208845854086540220230493287
q = 65746849928900354177936765297
phi = (p-1)*(q-1)
d = gmpy2.invert(e, phi)
pt = long_to_bytes(pow(c, d, n))
print(pt)