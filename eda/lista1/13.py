n = int(input())

c = int(input())
while(c != n):
    if c < n:
        print("O número correto é maior.")
    elif c > n:
        print("O número correto é menor.")
    c = int(input())
print("Parabéns! Você acertou.")
