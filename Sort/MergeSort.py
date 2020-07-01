"""
    1. Split origin array into 2 halves
    2. Use recursion to split 2 halves into array with single.
    3. Merge and sort for 2 halves.
    4. Check if left one or right one (half).

    TIME COMPLEXITY:
        + Best case: O(nlogn)
        + Worst case: O(nlogn)
        + Average case: O(nlogn)
    
    SPACE COMPLEXITY: O(n)

    NOTE:
    Time complexity of Merge Sort is O(n*Log n) in all the 3 cases (worst, average and best) as merge sort always divides the array in two halves and takes linear time to merge two halves.
    It requires equal amount of additional space as the unsorted array. Hence its not at all recommended for searching large unsorted arrays.
    It is the best Sorting technique used for sorting Linked Lists.
"""

import sys
sys.path.append("D:/DSaAlgo")

def mergeSort(arr):
    # Base case
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[mid:]
        R = arr[:mid]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
    from read_sample import ReadSampleData
    arr = ReadSampleData()
    print(arr)
    mergeSort(arr)
    print(arr)