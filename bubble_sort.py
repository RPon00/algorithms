"""
A practice implementation of bubble sort.
"""

def non_increasing(a, b):
    """ Returns true if the elements are in non-increasing order. """
    return a >= b

def non_decreasing(a, b):
    """ Returns true if the elements are in non-decreasing order. """
    return a <= b

def bubble_sort(input, compare=non_decreasing):
    """ 
    The classic bubble sort algorithm.

    Arguments:
    input -- the list of numbers to be sorted

    Keyword Arguments:
    compare(a, b) -- function, returns true if the two elements are in order 

    >>> example = [9, 1, 4, 7, 2]
    >>> bubble_sort(example, non_increasing)
    [9, 7, 4, 2, 1]
    >>> bubble_sort(example)
    [1, 2, 4, 7, 9]
    """
    list_len = len(input)
    for num_sorted in xrange(list_len - 1):
        # subtract num_sorted from inner loop -- end is already sorted
        for i in xrange(0, list_len - num_sorted - 1):
            # test if the element should be swapped with next element
            if not compare(input[i], input[i+1]):
                input[i], input[i+1] = input[i+1], input[i] 
    return input

if __name__ == "__main__":
    # a check to make sure that docs are up to date
    import doctest
    doctest.testmod()
