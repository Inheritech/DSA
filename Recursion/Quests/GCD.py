def gdc(a, b):
    if not isinstance(a, int):
        raise ValueError('First number input has to be an integer.')
    if not isinstance(b, int):
        raise ValueError('Second number input has to be an integer.')
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gdc(b, a % b)

print(gdc(10, 15))
print(gdc(0, 5))