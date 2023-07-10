# python write byte to file

import os

payload  = b'a'*32 + b'\xef\xbe\xad\xde'

def write_byte_to_file(file_path, byte):
    with open(file_path, 'wb') as f:
        f.write(byte)
        

def write_byte_to_file_append(file_path, byte):
    with open(file_path, 'ab') as f:
        f.write(byte)

write_byte_to_file('payload', payload)