"""
1.0 7.0
5.0 9.0
2j
4.4721
2.0000
4.4721
0 2
2.0000
-2.5 0.4
12.1 7.3
1+2j
16.1484
2.2361
16.1484
1 2
2.2361
2.5 -0.4
-12.2 7.0
3+4j
16.4575
5.0000
16.4575
3 4
5.0000
0.0 0.0
0.0 1.0
0
1.0000
0.0000
1.0000
0 0

***Error***
Traceback (most recent call last):
  File "__tester__.python3", line 23, in <module>
    z = (a**2 + b**2)**(1/2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
"""

x1, y1 = input().split()
x1, y1 = [float(x1), float(y1)]

x2, y2 = input().split()
x2, y2 = [float(x2), float(y2)]

distance = ((x2 - x1)**2 + (y2 - y1)**2 )**(1/2)

print("{:.4f}".format(distance))

c = str(input())
a, b = 0, 0
if "+" in c:
    a, b = c.split("+")
    a = int(a)
    b = int(b.strip("j"))
elif "j" in c:
    b = int(c.strip("j"))
else:
    a = c

z = 0
if a != b and b!=0:
    z = (a**2 + b**2)**(1/2)
print("{:.4f}".format(z))
