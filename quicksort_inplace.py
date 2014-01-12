
import random

def quicksort(arr, left=0, right=None):
    if right is None: right = len(arr) - 1
    if right + 1 - left < 2: return

    pivotIndex = random.randint(left, right)
    newPivotIndex = partition(arr, left, right, pivotIndex)
    quicksort(arr, left, newPivotIndex - 1)
    quicksort(arr, newPivotIndex + 1, right)

def partition(arr, left, right, pivotIndex):
    pivotVal = arr[pivotIndex] 
    swap(arr, pivotIndex, right)
    storedIndex = left
    for i in xrange(left, right):
        if (arr[i] <= pivotVal):
            swap(arr, i, storedIndex)
            storedIndex += 1
    swap(arr, storedIndex, right)
    return storedIndex

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

for i in xrange(1,10):
    arr = [random.randint(0, 1000) for k in xrange(1,1000)]
    quicksort(arr)
    a2 = sorted(arr)
    assert (arr == a2), (arr, a2)