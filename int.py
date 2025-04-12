import sys
import ctypes


v=20
def inspect_int(n):
    address=id(n)
    size=sys.getsizeof(n)
    raw=(ctypes.c_ubyte * size).from_address(address)
    #print(f"address: {address}, size: {size}, raw: {raw}")
    print(f"int:{n}, address:{(address)}, size{size}")
    print("raw memory:", list(raw))


print(inspect_int(v))