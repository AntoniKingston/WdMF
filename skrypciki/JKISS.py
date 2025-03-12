import struct
import sys
def generator(n, x = 123456789, y = 987654321, z = 432198765, c = 6543217):
    # rang = max-min
    mask = 0xFFFFFFFF
    maxp1 = 2**32
    for i in range(n):
        x = (314527869 * x +1234567) & mask
        y ^= (y << 5) & mask
        y ^= (y >> 7) & mask
        y ^= (y << 22) & mask
        t = 4294584393 * z + c
        c = t >> 32
        rand = (x + y + z) & mask
        print(rand)
        # sys.stdout.buffer.write(struct.pack('<I', rand))

generator(100)

