import math

x, y = input().split()
x, y = [int(x), int(y)]

a = math.gcd(x, y)
print(a)
