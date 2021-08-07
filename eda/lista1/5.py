n = int(input())

for i in range(n):
    x, y = input().split()
    x, y = [int(x), int(y)]

    s = 0
    for j in range(x, x+2*y):
        if j % 2 == 1:
            s += j

    if i == 0:
        min_sum = s
        max_sum = s

    if s < min_sum:
        min_sum = s
    if s > max_sum:
        max_sum = s

    print(s)

print(max_sum)
print(min_sum)
avg =(min_sum + max_sum)/2
print("{:.2f}".format(avg))
