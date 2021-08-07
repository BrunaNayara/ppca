class Stack():
    s = 0
    items = []

    def push(self, item):
        self.items.append(item)
        self.s += 1
        return self.items

    def pop(self):
        i = self.items.pop()
        self.s -= 1
        return i

    def size(self):
        return self.s

    def isEmpty(self):
        return self.s == 0


def operacao(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b


exp = input().split()

operadores = "+-*"
stack = Stack()

for c in exp:

    if c not in operadores:
        stack.push(c)
    else:
        a = int(stack.pop())
        b = int(stack.pop())
        op = c
        resultado = operacao(a, b, op)
        stack.push(resultado)

print(stack.pop())
