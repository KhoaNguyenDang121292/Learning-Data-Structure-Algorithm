def ReadSampleData():
    with open("test_data.txt", "r") as f:
        arr = f.readline().split()
        arr = list(map(int, arr))
    return arr


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


def BubbleSortOptimize(arr):
    i = len(arr) - 1
    flag = 0 # Flag for swap or not
    while i >= 0:
        for j in range(0, i, +1):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == 0:
            break
        i -= 1


if __name__ == "__main__":
    arr = ReadSampleData()
    BubbleSortOptimize(arr)
    print(arr)