def SelectionSort(arr):
    minPos = 0
    i = len(arr) - 1
    while i >= 1:
        if arr[i] < minElement:
            arr[i], minElement = minElement, arr[i]