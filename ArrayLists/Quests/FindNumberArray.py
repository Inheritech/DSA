import numpy as np
import random

def gen_random(n):
    return random.sample(range(n * 10), n)

def binary_search(arr, n):
    sorted_arr = sorted(arr)
    current_search_size = len(arr) // 2
    current_index = current_search_size
    while current_search_size > 0:
        current_value = sorted_arr[current_index]
        if current_value == n:
            return True
        current_search_size //= 2
        if current_value > n:
            current_index -= current_search_size
        else:
            current_index += current_search_size
    return False

def loop_search(arr, n):
    return n in arr

def numpy_search(arr, n):
    np_arr = np.array(arr)
    return n in np_arr

def test_both(size, n):
    import timeit
    rand_list = gen_random(size)
    glob = globals()
    glob['rand_list'] = rand_list
    glob['n'] = n
    print("Binary with size {}".format(size), timeit.timeit("binary_search(rand_list, n)", globals = glob, number = 100))
    print("Loop with size {}".format(size), timeit.timeit("loop_search(rand_list, n)", globals = glob, number = 100))
    print("Numpy with size {}".format(size), timeit.timeit("numpy_search(rand_list, n)", globals = glob, number = 100))

if __name__ == '__main__':
    size = 100
    for i in range(4):
        test_both(size, 100)
        size *= 10