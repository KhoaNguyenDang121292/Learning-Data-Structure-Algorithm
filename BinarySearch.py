# Best case:
# Worst case:
# Average case:
# Time complexity:
# Space complexity:
from read_sample import ReadSampleData

def BinarySearch(arr, k):
    left = 0
    right = len(arr) - 1
    mid = (left + right)//2
    i = 0
    while i < len(arr):
        if k > arr[mid]:
            left = mid + 1
        if k < arr[mid]:
            right = mid - 1
        mid = (left + right)//2
        if k == arr[mid]:
            return mid
        i += 1
    return -1

if __name__ == "__main__":
    arr = ReadSampleData()
    k = 20
    print(arr)
    position = BinarySearch(arr, k)
    print("Position: " + str(position))