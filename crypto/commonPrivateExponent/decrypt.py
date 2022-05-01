from Crypto.Util.number import *
import fpylll

# https://github.com/fplll/fpylll
e1 = 587438623 
n1 = 2915050561
e2 = 2382816879
n2 = 3863354647
e3 = 2401927159
n3 = 3943138939
plain = 62794
ct = pow(plain, e1, n1)
ct2 = pow(plain, e2, n2)
B = [[plain,e1,e2,e3],
    [0,-n1,0,0],
    [0,0,-n2,0],
    [0,0,0,-n3]]


M = fpylll.IntegerMatrix.from_matrix(B)
reduced_basis = fpylll.LLL.reduction(M)
print("reduced basis:")
print(reduced_basis)
for i in range(4):
    sum = 1
    for j in range(4):
        sum *= reduced_basis[i][j]
    print(sum)


d = abs(reduced_basis[0][0])/B[0][0]
print(f"smallest basis vector: {reduced_basis[0]}")
pt = pow(ct, int(d), n1)
pt2 = pow(ct2, int(d), n2)
print(f"d: {d}", f"pt: {pt}", f"pt2: {pt2}")