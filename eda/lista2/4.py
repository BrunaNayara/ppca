f = [0 for i in range(50000)]
f[1] = 1
f[2] = 1

def fib(n):
    if f[n] != 0:
        return f[n]
    f[n] = fib(n-2) + fib(n-1)
    return f[n]

a = int(input())
r = fib(a)
print(r)
