import sys
sys.path.append("D:/DSaAlgo")

def rightRotation(arr):
    temp = arr[len(arr)-1]
    i = len(arr) - 1
    while i >= 0:
        arr[i] = arr[i-1]
        i -= 1
    arr[0] = temp

def leftRotation(arr):
    temp = arr[0]
    i = 0
    while i < len(arr)-1:
        arr[i] = arr[i + 1]
        i += 1
    arr[i] = temp

def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Rotation using Reverse 3 times
    # First reverse: ArB
    # Second reverse: ArBr
    # Third reverse: (ArBr)r
def reverseArray(arr, d):
    reverse(arr, 0, d-1)
    reverse(arr, d, len(arr)-1)
    reverse(arr, 0, len(arr)-1)

if __name__ == "__main__":
    from read_sample import ReadSampleData
    arr = ReadSampleData()
    print("Array before rotated: " + str(arr))
    reverseArray(arr, 2)
    print("Array after rotated: " + str(arr))