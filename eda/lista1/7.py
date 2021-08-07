def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    return -1

x = int(input())
y = int(input())

a = compare(x, y)

if a == 1:
    print("x e maior que y")
elif a == 0:
    print("x e igual a y")
else:
    print("x e menor que y")
