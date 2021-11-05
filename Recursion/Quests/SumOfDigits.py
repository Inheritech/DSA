# How would you find the sum of digits of a positive integer number using recursion?

def sum_of_digits(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError('The input must be a positive integer number')
    if n < 10:
        return n
    return n % 10 + sum_of_digits(int(n / 10))

print(sum_of_digits(102))