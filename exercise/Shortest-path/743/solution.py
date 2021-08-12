from heapq import *

class Graph:

    def __init__(self, size):
        self._graph = [{} for _ in range(0, size + 1)]

    def add(self, f, t, w):
        self._graph[f][t] = w

    def dijkstra(self, v):
        candidates = []
        reached = set()
        all_dis = [100000000 for _ in range(len(self._graph))]
        all_dis[v] = 0
        heappush(candidates, (0, v))
        while len(candidates) > 0:
            dis, t = heappop(candidates)
            if t in reached:
                continue
            reached.add(t)
            for node, l in self._graph[t].items():
                if dis + l < all_dis[node]:
                    all_dis[node] = dis + l
                    heappush(candidates, (all_dis[node], node))
        result = 0
        for dis in all_dis[1:]:
            if dis > result:
                result = dis
        if result == 100000000:
            return -1
        else:
            return result



class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = Graph(N)
        for edge in times:
            g.add(edge[0], edge[1], edge[2])
        return g.dijkstra(K)
