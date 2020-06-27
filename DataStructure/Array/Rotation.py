"""
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
                print("Zo")
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

if __name__ == "__main__":
    arr = ReadSampleData()
    print("Array before rotated: " + str(arr))
    d = 5
    n = len(arr)
    print("Aray length: " + str(n))
    # leftRotate(arr, d, n)
    # print("Array after left rotated: " + str(arr))
    jugglingRotate(arr, d, n)
    print("Array after rotated: " + str(arr))
