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


close_chars = ")]}"
open_chars = "([{"

parenteses = "()"
colchetes = "[]"
chaves = "{}"

exp = input()

stack = Stack()
ok = True

for c in exp:
    if c in open_chars:
        stack.push(c)
    elif c in close_chars:
        topo = stack.pop()
        if c in parenteses and topo not in parenteses:
            ok = False
            break
        if c in colchetes and topo not in colchetes:
            ok = False
            break
        if c in chaves and topo not in chaves:
            ok = False
            break

print(ok)
