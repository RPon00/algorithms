

def binary_search(sorted_list, target):
    """
    """
    imin, imax = 0, len(sorted_list)
    while imax >= imin:
        mid = (imax + imin) / 2
        mid_val = sorted_list[mid]
        if mid_val < target:
            imin = mid + 1
        elif mid_val > target:
            imax = mid - 1
        else:
            return mid
    return None

if __name__ == '__main__':
    from random import randint
    a = sorted(set([randint(0, 10000000) for _ in xrange(10000)]))
    for i, n in enumerate(a):
        assert i == binary_search(a, n)