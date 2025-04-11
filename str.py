import sys

#import ctypes
# import emoji


str1="aaa"
str2="aa🪛"

str3="ыыы"
str31="ыыы"*10
str4="ыы😶‍🌫️"
str41="ыы😶‍🌫️"*1945


size_str1=sys.getsizeof(str1)
size_str2=sys.getsizeof(str2)
size_str3=sys.getsizeof(str3)
size_str31=sys.getsizeof(str31)
size_str4=sys.getsizeof(str4)
size_str41=sys.getsizeof(str41)

print(str1, size_str1)
print(str2, size_str2)
print(str3, size_str3)
print(str31, size_str31)
print(str4, size_str4)
print(size_str41)
print(hash(str4), hash(str41))

x=10**9

str42="ыы😶‍🌫️"*x
print(sys.getsizeof(str42))