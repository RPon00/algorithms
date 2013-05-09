
from heapq import heappush, heappop

class Node(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.dist = float("inf")
        self.prev = None

def dijkstra(source):
    unvisited = [(0, source)]
    source.dist = 0
    visited_set = set()
    while unvisited:    # could just use a try/except IndexError
        _, node = heappop(unvisited)
        if node.dist == float("inf"):
            return
        visited_set.add(node)
        for neighbor, weight in ((n, w) for n, w in node.neighbors 
                                  if n not in visited_set):
            new_weight = node.dist + weight
            if new_weight < neighbor.dist:
                neighbor.dist = new_weight
                neighbor.prev = node
                heappush(unvisited, (new_weight, neighbor))

def spfa(source):
    source.dist = 0
    queue = [source]
    q_set = set(queue)
    while queue:
        node = queue.pop(0)
        q_set.remove(node)
        for vert, w in node.neighbors:
            new_weight = node.dist + w
            if new_weight + w < vert.dist:
                vert.prev = node
                vert.dist = new_weight
                if vert not in q_set:
                    q_set.add(vert)
                    queue.append(vert)

def link(a, b, weight):
    a.neighbors.append((b, weight))
    b.neighbors.append((a, weight))

def prep():
    a = Node('1')
    b = Node('2')
    c = Node('3')
    d = Node('4')
    e = Node('5')
    f = Node('6')

    link(a, b, 10)
    link(a, c, 9)
    link(a, f, 14)

    link(b, c, 10)
    link(b, d, 15)

    link(c, f, 2)
    link(c, d, 11)

    link(d, e, 6)

    link(f, e, 9)

    return a, e

if __name__ == "__main__":
    source, sink = prep()
    spfa(source)

    node = sink
    tot = 0
    print 'tot:', node.dist
    while node is not None:
        print node.name
        node = node.prev

    print
    source, sink = prep()
    dijkstra(source)

    node = sink
    tot = 0
    print 'tot:', node.dist
    while node is not None:
        print node.name
        node = node.prev