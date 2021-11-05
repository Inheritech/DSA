def quick_sort(arr, start = 0, end = None):
    if len(arr) == 1:
        return

    if end is None:
        end = len(arr) - 1

    def partition(arr, low, high):
        small_i = low - 1 # Set the small number index to low - 1 so we don't go out of bounds when we increment it later
        pivot = arr[high] # Pivot as last element in partition

        for idx in range(low, high): # For each element in partition
            if arr[idx] <= pivot: # If the current element is less than pivot
                small_i += 1 # Increase the size of the small side (Left)
                arr[small_i], arr[idx] = arr[idx], arr[small_i] # Swap this element with the next element to the small number index (Swap with a bigger number than pivot)
        arr[small_i + 1], arr[high] = arr[high], arr[small_i + 1] # Swap the next biggest number with the pivot and keep small numbers to the left and big numbers to the right
        return small_i + 1 # Return the index of where the pivot ended (So the left and right side are partitioned now)

    if start < end:
        partition_index = partition(arr, start, end)

        quick_sort(arr, start = start, end = partition_index - 1)
        quick_sort(arr, start = partition_index + 1, end = end)


if __name__ == '__main__':
    arr = [3, 5, 8, 1, 2, 9, 4, 7, 6]
    quick_sort(arr)
    print(arr)
