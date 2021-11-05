def insertion_sort(arr):
    arr_len = len(arr)
    sorted_len = 0
    comparator = lambda left, right: left < right
    while sorted_len < arr_len:
        next = arr[sorted_len]
        print(arr)
        for test_index in range(sorted_len):
            if comparator(next, arr[test_index]):
                for shift_index in range(sorted_len, test_index, -1):
                    arr[shift_index] = arr[shift_index - 1]
                arr[test_index] = next
                break
        sorted_len += 1

if __name__ == '__main__':
    arr = [5, 3, 4, 7, 2, 8, 6, 9, 1]
    insertion_sort(arr)
    print(arr)