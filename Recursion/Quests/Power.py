def power(n: int, p: int) -> int:
    if not isinstance(n, int):
        raise ValueError('Input base number has to be an integer.')
    if not isinstance(p, int) or p < 0:
        raise ValueError('Input p number has to be a positive integer.')
    if p == 0:
        return 1
    if p == 1:
        return n
    return n * power(n, p - 1)

print(power(2, 0))
print(power(2, 1))
print(power(2, 32))