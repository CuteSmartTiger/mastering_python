# 5.9. Reading Binary Data into a Mutable Buffer

import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# Here is an example that illustrates the usage:
# Write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)
# bytearray(b'Hello World')

print(buf[0:5])
# b'Hallo'

