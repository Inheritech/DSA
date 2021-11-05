def bubble_sort(arr):
    comparator = lambda left, right: left < right
    run = 1
    while run < len(arr):
        clean = True
        for i in range(len(arr) - run):
            if not comparator(arr[i], arr[i + 1]):
                clean = False
                left_value = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = left_value
        if clean:
            break
        run += 1

if __name__ == '__main__':
    arr = [3, 2, 1]
    bubble_sort(arr)
    print(arr)
