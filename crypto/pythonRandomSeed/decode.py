import random

ct = "MmypTSPBJ{q6k_e1s_q1Ld8I}"
pt = "FindITCTF{"
flag = ""
brute = """abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\\]^_`|~\}{\""""
while len(ct) != len(pt):
    for cc in brute:
        flag = pt + cc
        temp = ""
        random.seed("FINDIT")
        for f in flag:
            if f.islower():
                temp += chr((ord(f)-ord('a')+random.randrange(0,26))%26 + ord('a'))
            elif f.isupper():
                temp += chr((ord(f)-ord('A')+random.randrange(0,26))%26 + ord('A'))
            elif f.isdigit():
                temp += chr((ord(f)-ord('0')+random.randrange(0,10))%10 + ord('0'))
            else:
                temp += f
        if ct.startswith(temp):
            pt += cc
            print(pt)