"""
A practice implementation of selection sort.
"""

def gt(a, b):
    return a > b

def lt(a, b):
    return a < b

def selection_sort(input, compare=lt):
    """ 
    Basic selection sort algorithm.

    Arguments:
    input -- the list of numbers to be sorted

    Keyword Arguments:
    compare(a, b) -- function, returns true if the two elements are in order 

    >>> example = [9, 1, 4, 7, 2]
    >>> selection_sort(example, gt)
    [9, 7, 4, 2, 1]
    >>> selection_sort(example)
    [1, 2, 4, 7, 9]
    """
    list_len = len(input)
    for i in xrange(list_len - 1):
        # the index where the target, based on compare, resides 
        target_index = i
        for j in xrange(i+1, list_len):
            if not compare(input[target_index], input[j]):
                target_index = j
        # swap the target to the end of the sorted list
        input[i], input[target_index] = input[target_index], input[i]
    return input

if __name__ == "__main__":
    # a check to make sure that docs are up to date
    import doctest
    doctest.testmod()
