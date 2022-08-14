import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long

n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
e = 65537
# use msieve, yafu or factordb to factor small n
p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809
phi = (p-1)*(q-1)
d = gmpy2.invert(e, phi)
pt = long_to_bytes(pow(c, d, n))
print(pt)