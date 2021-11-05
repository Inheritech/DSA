import random

def gen_random(n):
    return random.sample(range(n * 10), n)

def are_permutation(first, second):
    if len(first) != len(second):
        return False
    def generate_lookup(string):
        str_lookup = {}
        for c in string:
            if c in str_lookup:
                str_lookup[c] += 1
            else:
                str_lookup[c] = 1
        return str_lookup
    first_str_lookup = generate_lookup(first)
    second_str_lookup = generate_lookup(second)
    if len(first_str_lookup) != len(second_str_lookup):
        return False
    for key in first_str_lookup:
        if key not in second_str_lookup:
            return False
        if first_str_lookup[key] != second_str_lookup[key]:
            return False
    return True

def are_permutation_sort(first, second):
    if len(first) != len(second):
        return True
    first.sort()
    second.sort()
    return first == second

def test_both_random(size):
    print("Using random of size {}".format(size))
    test_both(gen_random(size), gen_random(size))

def test_both(first, second):
    import timeit
    glob = globals()
    glob['first'] = [c for c in first]
    glob['second'] = [c for c in second]
    print("Dictionary: ", timeit.timeit("are_permutation(first, second)", globals = glob, number = 100))
    print("Sort: ", timeit.timeit("are_permutation_sort(first, second)", globals = glob, number = 100))

if __name__ == '__main__':
    size = 10
    for i in range(3):
        test_both_random(size)
        size *= 10
    test_both("pparapa", "psdasds")
    test_both("darkhold", "dlohkrad")