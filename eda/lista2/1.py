def decimal2binario(d):
    if d == 0:
        return d
    b = bin(d).lstrip("0b")
    return b
