
def fib(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)

def fac(n):
    if n == 1:
        return 1
    return fac(n-1) * n

n = int(input())
a = fib(n)
b = fac(n)

if a % 2 == 1:
    print("{} {}".format(a, b))
else:
    print("{} {} {}".format(a, b, fib(n-1)))
