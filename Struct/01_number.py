"""
数字

整数
    byte 8位 -2^7-2^7-1
    short  16位 -2^15~2^15-1
    int  32位    -2^31~2^31-1
    long 64位    -2^63~2^64-1

二进制
0 2 4 8 16 32
    1 10
    10 1010
"""

# 与
print(0 & 0)  # 0
print(0 & 1)  # 0
print(1 & 1)  # 1

# 或
print(0 | 0)  # 0
print(0 | 1)  # 1
print(1 | 1)  # 1

# 异或
# 两个值结果相同,是0
# 两个值结果不相同,是1
print(0 ^ 0)  # 0
print(0 ^ 1)  # 1
print(1 ^ 1)  # 0

# 左移  乘
# 4 100  1000 8
print(4 << 1)  # 8

# 4* 2^2
print(4 << 2)  # 16

# -4 1100  110000  -16
print(-4 << 2)

# 右移  除
# 4 100  10 2
print(4 >> 1)  # 2

# 4//2^2  1
print(4 >> 2)  # 1

# 1100 1010   1001
print(-4 >> 2)  # -1
