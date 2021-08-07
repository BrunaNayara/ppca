primeiro = int(input())
max_n = primeiro

for i in range(9):
    a = int(input())
    if a > max_n:
        max_n = a

print(max_n)
if max_n % primeiro == 0:
    print(primeiro)
