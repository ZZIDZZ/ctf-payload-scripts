from pwn import *

# local process environment
io = process('./chal')

#remote process environment
#io = remote('ip',port)

# send payload 
io.sendlineafter(b':', b'AAAAAAA')

print(io.recvall().decode())