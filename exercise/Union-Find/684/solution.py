class Union:

    def __init__(self, size):
        self.root = [i for i in range(size + 1)]

    def add(self, a, b):
        self.root[self.find(b)] = self.find(a)

    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def same(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        all_union = Union(len(edges))
        for edge in edges:
            if all_union.same(*edge):
                return edge
            else:
                all_union.add(*edge)
        return []
        
