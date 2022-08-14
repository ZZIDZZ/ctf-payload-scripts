from Crypto.Util.number import long_to_bytes
import gmpy2

n = 5820149091210667720890225927235582400139169177352854426798008403514241143472827998429255513411050730963480848204846652190625554537556629487358188989021249
asd = 106853332652432478823479268251952762332539847111872583298926285910844066620524275860449200877961470156007933663569740467088542775307801035926875522276491129471033754427069136664680585101128413760373262347104521736750958041229560781277160132457139060114077575090698553884062695463643144131656598068508777247965320804974742245687176962336
c = 3648943329727253834409980203486664443818644290442599627700133917785183046282318039774935297399643661326653263568970101401829584333643972096205672660917351
e = 7

for i in range(0, 10000):
    root, isExact = gmpy2.iroot(i*n + c, e)
    if isExact:
        print(f"Found root: {i} {long_to_bytes(root)}")
    