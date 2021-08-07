def concat(a, b):
    if not a:
        return b
    else:
        return a[0:1] + concat(a[1:], b)

s1 = input()
s2 = input()

print(concat(s1, s2))
print(s1[len(s1)::-1])

if s1 in s2[0:len(s1)]:
    print("True")
else:
    print("False")
