from math import sqrt, ceil
from BubbleSort import bubble_sort

def bucket_sort(arr):
    arr_len = len(arr)
    bucket_num = round(sqrt(arr_len))
    buckets = []

    for i in range(bucket_num):
        buckets.append([])

    def get_max(arr):
        max = 0
        for n in arr:
            if max < n:
                max = n
        return max

    arr_max = get_max(arr)
    for n in arr:
        target_bucket = ceil(n * bucket_num / arr_max)
        buckets[target_bucket - 1].append(n)

    resulting_arr = []
    for bucket_i in range(bucket_num):
        bubble_sort(buckets[bucket_i])
        resulting_arr.extend(buckets[bucket_i]) # Could also apply to original arr
    return resulting_arr

if __name__ == '__main__':
    arr = [5, 3, 4, 7, 2, 8, 6, 9, 1]
    arr = bucket_sort(arr)
    print(arr)