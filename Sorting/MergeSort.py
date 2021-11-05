def merge_sort(arr):
    if len(arr) < 2:
        return arr
    first_half_len = len(arr) // 2
    first_half = arr[:first_half_len]
    second_half = arr[first_half_len:]
    def merge(left, right):
        result = []
        left_i = 0
        right_i = 0
        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                result.append(left[left_i])
                left_i += 1
            else:
                result.append(right[right_i])
                right_i += 1
        if left_i < len(left):
            result.extend(left[left_i:])
        if right_i < len(right):
            result.extend(right[right_i:])
        return result
    return merge(merge_sort(first_half), merge_sort(second_half))

if __name__ == '__main__':
    arr = [6, 4, 3, 7, 5, 1, 2]
    print(merge_sort(arr))
