"""
    TUTORIAL: https://www.geeksforgeeks.org/array-data-structure/
    KEY CONCEPT:
    SOLUTION 1:
        Using temp array
        - Input:  
            + Array: 1 2 3 4 5 6 7
            + Rotation: 2 (Quantity of element for starting rotation)
        - Output: 3 4 5 6 7 1 2
        TIME COMPLEXITY: O(n)
        Auxiliary Space: O(d)

    SOLUTION 2:
        Rotate one by one
        TIME COMPLEXITY: O(n*d)
        Auxiliary Space: O(1)
    
    SOLUTION 3:
        Juggling algorithm
        Find GCD: Greatest common divisor
        TIME COMPLEXITY: O(n)
        Auxiliary Space: O(1)

    SOLUTION 4:
        Block swap algorithm (Cache friendly more than Juggling)
        Find GCD: Greatest common divisor
        TIME COMPLEXITY: O(n)
        Auxiliary Space: O(1)
"""
import sys
sys.path.append("D:/DSaAlgo")

from read_sample import ReadSampleData

def tempRotate(arr):
    rotation = 1
    if rotation > len(arr):
        print("Rotation value is not grater than array length!")
    else:
        firstHalf = arr[0:rotation]
        secondHalf = arr[rotation:len(arr)]
        arrRotated = secondHalf + firstHalf
        print("Array after rotated: " + str(arrRotated))

def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(0, n-1, +1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def leftRotate(arr, d, n):
    for i in range(0, d, +1):
        leftRotateByOne(arr, n)

def jugglingRotate(arr, d, n):
    from Math.GCD import euclideanGCD
    d = d%n
    gcd = euclideanGCD(d, n)
    for i in range(0, gcd, +1):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def blockSwap(arr, fi, si, d):
    for i in range(0, d, +1):
        arr[fi + i], arr[si + i] = arr[si + i], arr[fi + i]

def blockSwapRotate(arr, d, n):
    if d == 0 or d == n:  
        return
    i = d
    j = n - d
    while i != j:
        if i < j: # A is shorter
            blockSwap(arr, d - i, d + j - i, i)
            j -= i
        else: # B is shorter
            blockSwap(arr, d - i, d, j)
            i -= j
    blockSwap(arr, d - i, d, i)

def cycleRotateByOne(arr, n):
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
        i += 1
    arr[0] = temp

if __name__ == "__main__":
    # arr = ReadSampleData()
    # print("Array before rotated: " + str(arr))
    # d = 5
    # n = len(arr)
    # print("Aray length: " + str(n))
    # # leftRotate(arr, d, n)
    # # print("Array after left rotated: " + str(arr))
    # # jugglingRotate(arr, d, n)
    # # print("Array after rotated: " + str(arr))
    # # blockSwapRotate(arr, d, n)
    # cycleRotateByOne(arr, len(arr))
    # print(arr)
