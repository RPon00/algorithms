


def all_pairs_shortest_paths(matrix):
    num_vertices = len(matrix)
    dist = matrix
    rng = range(num_vertices)
    for i in rng:
        for j in rng:
            for k in rng:
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
    return dist

def setup_graph():
    O = float("inf")    # for the sake of graph clarity
    graph = [
        [O, O, -2, O],
        [4, O, 3, O],
        [O, O, O, 2],
        [O, -1, O, O]
    ]
    return graph

if __name__ == "__main__":
    print all_pairs_shortest_paths(setup_graph())