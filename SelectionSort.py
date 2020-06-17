# Best case: 
# Worst case: 
# Average case: 
# Time complexity: O(n2)
# Space complexity: 

from read_sample import ReadSampleData

def SelectionSortAsc(arr):
    i = 0
    while i <= len(arr) - 1:
        minPos = i
        for j in range(i+1, len(arr), +1):                                                                                                                                                                 
            if arr[j] < arr[minPos]:
                arr[j], arr[minPos] = arr[minPos], arr[j]
        i += 1

def SelectionSortDesc(arr):
    i = 0
    while i <= len(arr) - 1:
        minPos = i
        for j in range(i+1, len(arr), +1):
            if arr[j] > arr[minPos]:
                arr[j], arr[minPos] = arr[minPos], arr[j]
        i += 1

def SelectionSortOptimizeAsc(arr):
    

if __name__ == "__main__":
    arr = ReadSampleData()
    SelectionSortDesc(arr)
    print(arr)