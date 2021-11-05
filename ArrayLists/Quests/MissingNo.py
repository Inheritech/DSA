mylist = [i for i in range(100) if i != 73]

def test_weird():
    findMissing(mylist, 100)

def test_useful():
    find_missing_seq(mylist)

def findMissing(list, n):
    sum1 = 100*101/2
    sum2 = sum(list)
    return sum1 - sum2

def find_missing_seq(arr):
    last = arr[0]
    for el in arr:
        if el == last:
            continue
        next = last + 1
        if el != next:
            return next
        last = next

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test_weird()", globals = locals()))

    print(timeit.timeit("test_useful()", globals = locals()))