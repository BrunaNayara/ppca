def operacao(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b

ops = "+-*"
exp = input().split()
pilha = []

while(len(exp)):
    print("exp")
    print(exp)
    j = exp[0]
    while(j not in ops):
        print("pilha")
        print(pilha)
        pilha.append(j)
        j = exp.pop(0)
    else:
        a = int(pilha.pop())
        print("aaaaa")
        print(a)
        b = int(pilha.pop())
        c = operacao(a, b, j)
        pilha.append(c)

        print(c)
