def BubbleSortAsc(arr):
    i = len(arr) - 1
    while i >= 0:
        for j in range(0, i, +1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        i -= 1


def BubbleSortDesc(arr):
    i = len(arr) - 1
    while i >= 0:
        for j in range(0, i, +1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        i -= 1


if __name__ == "__main__":
    arr = [3,44,38,5,47,15,36,26,27,2,46,4,19]
    BubbleSortAsc(arr)
    print(arr)