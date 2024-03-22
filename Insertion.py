def insertion_sort(arr):
    size = len(arr)
    for i in range(size):
        bia = i
        while bia > 0 and arr[bia-1] > arr[bia]:
            arr[bia-1], arr[bia] = arr[bia], arr[bia-1]
            bia -= 1