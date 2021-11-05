def selection_sort(arr):
    arr_len = len(arr)
    sorted_len = 0
    comparator = lambda left, right: left < right
    while sorted_len < arr_len:
        min_index = sorted_len
        for i in range(sorted_len + 1, arr_len):
            if comparator(arr[i], arr[min_index]):
                min_index = i
        if sorted_len == min_index:
            sorted_len += 1
            continue
        left_value = arr[sorted_len]
        arr[sorted_len] = arr[min_index]
        arr[min_index] = left_value
        sorted_len += 1

if __name__ == '__main__':
    arr = [5, 7, 4, 3, 8, 6, 1, 9, 2]
    selection_sort(arr)
    print(arr)