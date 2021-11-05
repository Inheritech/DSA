from BinaryHeap import Heap

def heap_sort(arr):
    heap = Heap()
    for n in arr:
        heap.add(n)
    result = []
    while heap.peek():
        result.append(heap.extract())
    return result

if __name__ == '__main__':
    arr = [2, 1, 7, 6, 5, 3, 45, 7, 8, 1, 53]
    print(heap_sort(arr))
