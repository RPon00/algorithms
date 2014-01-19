from collections import deque

class PairingHeap(object):
    """ http://en.wikipedia.org/wiki/Pairing_heap """
    def __init__(self):
        self.root = None
        self.len = 0

    def find_min(self):
        if not self.len:
            raise IndexError, 'The heap is empty.'
        return self.root.elem

    def delete_min(self):
        if not self.len:
            raise IndexError, 'The heap is empty.'
        self.len -= 1
        self.root = self._merge_pairs(self.root.subheaps)

    def insert(self, elem):
        self.len += 1
        self.root = self._merge(self.root, PairingHeapNode(elem, []))

    def _merge(self, heap1, heap2):
        if not (heap1 and heap2):
            return heap1 or heap2

        sm_h, big_h = heap1, heap2
        if sm_h.elem > big_h.elem:
            sm_h, big_h = big_h, sm_h 
        sm_h.subheaps.append(big_h)
        return sm_h

    def _merge_pairs(self, heaps):
        if not heaps:
            return
        len_heaps = len(heaps)
        if len_heaps is 1:
            return heaps[0]

        # merge every other pair
        paired = deque()
        for ptr in xrange(0, len_heaps - 1, 2):   # do inline merge
            heap1, heap2 = heaps[ptr], heaps[ptr+1]
            if heap1.elem < heap2.elem:
                heap1.subheaps.append(heap2)
                paired.append(heap1)
            else:
                heap2.subheaps.append(heap1)
                paired.append(heap2)
        if len_heaps % 2:
            paired.append(heaps[-1])

        # merge final pair with all other pairs
        final_heap = paired.pop()
        for heap in paired:    # do inline merge
            if heap.elem < final_heap.elem:
                heap.subheaps.append(final_heap)
                final_heap = heap
            else:
                final_heap.subheaps.append(heap)
        return final_heap

    def __len__(self):
        return self.len

class PairingHeapNode(object):
    __slots__ = ['elem', 'subheaps']
    def __init__(self, elem, subheaps):
        self.elem = elem
        self.subheaps = subheaps


def main():
    from random import randint 

    ph = PairingHeap()
    for x in xrange(10000):
        ph.insert(randint(0, 1e8))

    sorted_arr = []
    while ph:
        sorted_arr.append(ph.find_min())
        ph.delete_min()
    # print sorted_arr
    assert sorted_arr == sorted(sorted_arr)

if __name__ == '__main__':
    main()