def to_binary(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input number must be a positive integer")
    if n == 0:
        return 0
    return n % 2 + 10 * to_binary(n // 2)

print(to_binary(10))
print(to_binary(13))