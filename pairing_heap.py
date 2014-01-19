
class PairingHeap(object):
    """ http://en.wikipedia.org/wiki/Pairing_heap """
    def __init__(self, elem, subheaps):
        self.elem = elem
        self.subheaps = subheaps

def find_min(heap):
    if not heap:
        raise IndexError, 'The heap is empty.'
    return heap.elem

def delete_min(heap):
    if not heap:
        raise IndexError, 'The heap is empty.'
    return merge_pairs(heap.subheaps)

def insert(heap, elem):
    return merge(heap, PairingHeap(elem, []))

def merge(heap1, heap2):
    if not (heap1 and heap2):
        return heap1 or heap2
    elif heap1.elem < heap2.elem:
        return PairingHeap(heap1.elem, heap1.subheaps + [heap2])
    else:
        return PairingHeap(heap2.elem, heap2.subheaps + [heap1])
def merge_pairs(heaps):
  if not len(heaps):
    return
  elif len(heaps) is 1:
    return heaps[0]
  else:
    return merge(merge(heaps[0], heaps[1]), merge_pairs(heaps[2:]))


def test():
    from random import randint 

    ph = None
    for x in xrange(1000):
        ph = insert(ph, randint(0, 1000))

    sorted_arr = []
    while ph:
        sorted_arr.append( find_min(ph) )
        ph = delete_min(ph)

    assert sorted_arr == sorted(sorted_arr)

if __name__ == '__main__':
    test()