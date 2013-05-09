"""
A practice implementation of insertion sort.
"""

def insertion_sort(array):
    """ 
    Basic insertion sort algorithm.

    Arguments:
    array -- the list of numbers to be sorted

    >>> example = [9, 1, 4, 7, 2]
    >>> insertion_sort(example)
    [1, 2, 4, 7, 9]
    """
    for i in xrange(1, len(array)):
        val = array[i]
        hole = i
        while hole != 0 and val < array[hole-1]:
            array[hole] = array[hole-1]
            hole -= 1
        array[hole] = val
    return array

if __name__ == "__main__":
    # a check to make sure that docs are up to date
    import doctest
    doctest.testmod()
