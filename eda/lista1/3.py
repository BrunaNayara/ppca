"""
input
4
4
4
4
4
output
4.000

input
0
1
2
3
4.0
output
2.667

input
1.525
2
2
2
4.2
output
2.702
"""

soma = 0
for i in range(1, 6):
    a = float(input())
    soma = soma + a*i

result = soma/15
print('{:.3f}'.format(result))
