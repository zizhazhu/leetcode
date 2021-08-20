struct UnionFind {
    int root[1001];
    UnionFind() {
        for (int i = 0; i <= 1000; i++) root[i] = i;
    }
    int Find(int a) {
        if (root[a] != a)
            root[a] = Find(root[a]);
        return root[a];
    }
    void insert(int a, int b) {
        a = Find(a);
        b = Find(b);
        root[a] = b;
    }
    bool Same(int a, int b) {
        return Find(a) == Find(b);
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UnionFind unionFind;
        for (int i = 0; i < edges.size(); i++) {
            if (unionFind.Same(edges[i][0], edges[i][1])) {
                return edges[i];
            } else {
                unionFind.insert(edges[i][0], edges[i][1]);
            }
        }
        return vector<int>();
    }
};
