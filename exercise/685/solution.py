class UnionSet:
    def __init__(self, size):
        self._root = [i for i in range(size + 1)]

    def find(self, a):
        if self._root[a] != a:
            self._root[a] = self.find(self._root[a])
        return self._root[a]

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def add(self, a, b):
        self._root[self.find(b)] = self.find(a)

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        union_set = UnionSet(len(edges))
        critical = -1
        father_removed = -1, -1
        circle_father, circle_end = -1, -1
        for edge in edges:
            a, b = edge[0], edge[1]
            if union_set.find(a) == b:
                circle_father = b
                if critical != -1:
                    break
                else:
                    circle_end = a
            if union_set.find(b) != b:
                critical = b
                if circle_father != -1:
                    break
                father_removed = a
            else:
                union_set.add(a, b)
        if critical == -1:
            return [circle_end, circle_father]
        if circle_father != -1:
            for edge in edges:
                if edge[1] == critical:
                    return [edge[0], edge[1]]
        return [father_removed, critical]
