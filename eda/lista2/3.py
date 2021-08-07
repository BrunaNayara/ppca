def verificaParanteses(s):
    parenthesis = 0
    for c in s:
        if c == "(":
            parenthesis += 1
        if c == ")":
            parenthesis -= 1

        if parenthesis < 0:
            return False

    if parenthesis == 0:
        return True

    return False


s = input()
balanceado = verificaParanteses(s)
print(balanceado)

