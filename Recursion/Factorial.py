def factorial(n):
    if n < 0:
        raise ArithmeticError('Factorial can only be calculated for positive numbers but %d was provided.' % n)
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(3))