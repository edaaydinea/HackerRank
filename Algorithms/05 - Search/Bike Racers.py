# from sets import Set
def bipartiteMatch(graph):
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break

    while 1:
        preds = {}
        unmatched = []
        pred = dict([(u, unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)

        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v, []).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)

        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return matching, list(pred), list(unlayered)

        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)


def main():
    N, M, K = map(int, input().split())
    bikers = []
    bikes = []
    for i in range(N):
        a, b = map(int, input().split())
        bikers.append((a, b))
    for i in range(M):
        a, b = map(int, input().split())
        bikes.append((a, b))

    edges = []
    for (a, b) in bikers:
        for (c, d) in bikes:
            dist = (a - c) ** 2 + (b - d) ** 2
            edges.append((dist, (a, b), (c, d)))

    edges = sorted(edges, reverse=True)
    removed_bikers = 0
    removed_bikes = 0
    biker_hits = dict([(biker, 0) for biker in bikers])
    bike_hits = dict([(bike, 0) for bike in bikes])

    bikers = set(bikers)
    bikes = set(bikes)

    neighbors = dict([(biker, set([bike for bike in bikes])) for biker in bikers])
    G = dict([(biker, neighbors[biker]) for biker in bikers])
    (matching, A, B) = bipartiteMatch(G)
    matching_pairs = set([(bike, matching[bike]) for bike in matching])

    for (dist, biker, bike) in edges:
        biker_hits[biker] += 1
        bike_hits[bike] += 1
        neighbors[biker].remove(bike)

        if (bike, biker) in matching_pairs:
            G = dict([(biker, neighbors[biker]) for biker in bikers])
            (matching, A, B) = bipartiteMatch(G)
            matching_pairs = set([(bike, matching[bike]) for bike in matching])
            if len(matching.keys()) < K:
                print(dist)
                break

        if biker_hits[biker] == M:
            bikers.remove(biker)


if __name__ == "__main__":
    main()
