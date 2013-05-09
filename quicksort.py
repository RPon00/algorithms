
from random import randint

def quicksort(array):
    array_length = len(array)
    if array_length < 2:
        return array
    left = []
    right = []
    pivot = array.pop(randint(0, array_length-1))
    while array:
        val = array.pop()
        if val > pivot:
            right.append(val)
        else:
            left.append(val)
    return quicksort(left) + [pivot] + quicksort(right)

if __name__ == '__main__':
    print quicksort([1,7,3,9,2])