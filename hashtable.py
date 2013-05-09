
from __future__ import division
from math import floor
from itertools import izip

class HashTable(object):

    def __init__(self, capacity=2):
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.factor = self.calc_factor()
        self.load_factor = .75

    def __setitem__(self, key, value):
        if key is None:
            raise AttributeError    # TODO: find the correct expection for this
        self.size += 1
        index = self.hash_n_bits(key, self.factor)
        capacity = self.capacity
        while True:
            if self.keys[index] is None or self.keys[index] == key:
                self.keys[index] = key
                self.values[index] = value
                break
            else:
                index = (index + 1) % capacity
        self.resize()

    def __getitem__(self, key):
        index = self.hash_n_bits(key, self.factor)
        capacity = self.capacity
        step = 0
        while True:
            current_key = self.keys[index + step % capacity]
            if current_key == key:
                return self.values[index]
            step += 1
            if current_key is None or step == self.capacity:
                raise KeyError, key
            print 'wtf'

    def __contains__(self, key):
        index = self.hash_n_bits(key, self.factor)
        capacity = self.capacity
        step = 0
        while True:
            current_key = self.keys[index + step % capacity]
            if current_key == key:
                return True
            step += 1
            if current_key is None or step == self.capacity:
                return False

    def __delitem__(self, key):
        index = self.hash_n_bits(key, self.factor)
        capacity = self.capacity
        step = 0
        while True:
            current_key = self.keys[index + step % capacity]
            if current_key == key:
                self.keys[index + step % capacity] = None
                self.values[index + step % capacity] = None
                self.size -= 1
                self.resize()
                return
            step += 1
            if current_key is None or step == self.capacity:
                raise KeyError, key

    def calc_factor(self):
        f = 1
        while 2 ** f < self.capacity:
            f += 1
        return f
    
    def resize(self):
        old_kv = izip(self.keys, self.values)
        if self.size > self.capacity * self.load_factor:
            self.capacity *= 2
            self.repopulate(old_kv)
        elif self.size < self.capacity / 4:
            self.capacity = self.capacity // 2
            self.repopulate(old_kv)


    def repopulate(self, old_kv):
        self.factor = self.calc_factor()
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        for k,v in old_kv:
            if k is not None:
                self[k] = v

    def hash_n_bits(self, key, n):
        h = bin(hash(key))[2:]
        return int(h[-n:], 2)


if __name__ == "__main__":
    def main():
        from random import randint
        k = [n for n in xrange(10000)]
        v =[randint(0,10000) for n in xrange(10000)]
        h = HashTable()
        zkv = zip(k,v)
        for k,v in zkv:
            h[k] = v
        for k,v in zkv:
            assert h[k] == v, (k, v, h[k])

    import cProfile
    cProfile.run('main()', sort=2)