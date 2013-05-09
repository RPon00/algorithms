
from random import randint

def shuffle(source):
    for i in xrange(len(source)):
        k = randint(0, i)
        source[i], source[k] = source[k], source[i]
    return source

a = [randint(0,100000) for _ in xrange(1000)]
b = sorted(a)
assert sorted(shuffle(a)) == b