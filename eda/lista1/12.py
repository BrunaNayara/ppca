"""
2 3
2 3 ok
2 3 ok
3 1
3 1 errados
3 1 errados
5 5
5 5 ok
5 5 ok
5 4
5 4 errados
5 4 ok
5 4
5 4 errados
5 4 ok
9 9
9 9 ok
9 9 ok
0 0
0 0 errados
0 0 ok
0 1
0 1 ok
0 1 ok
1 0
1 0 errados
1 0 ok
89 25
89 25 errados
89 25 errados
4 5
4 5 ok
4 5 ok
10 12
10 12 errados
10 12 errados
10 11
10 11 ok
10 11 ok
11 10
11 10 errados
11 10 ok
"""

x, y = input().split()
x, y = [int(x), int(y)]

if y == 0:
    print("{} {} errados".format(x, y))
elif x == y or abs(y-x) <= 1 and x < y and y != 0:
    print("{} {} ok".format(x, y))
else:
    print("{} {} errados".format(x, y))
