

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) / 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else: 
            result.append(right.pop(0))
    result.extend(right)
    result.extend(left)
    return result

if __name__ == '__main__':
    from random import randint
    rng = 100000
    test = [randint(0, rng) for _ in xrange(rng)]
    assert merge_sort(test) == sorted(test)