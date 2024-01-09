def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(
            arr, n, largest
        )  # heapify call here is important to maintain heap property in the tree


def heap_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len // 2 - 1, -1, -1):
        heapify(arr, arr_len, i)

    for i in range(arr_len - 1, 0, -1):
        # Swapping the first element with the current element
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


x = [4, 10, 3, 5, 1]
print(x)
heap_sort(x)
print(x)
