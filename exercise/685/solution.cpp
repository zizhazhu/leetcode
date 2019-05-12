struct UnionSet {
    vector<int> father;
    UnionSet(int n): father(n) {}
    int root(int a) {
        if (father[a] != a) father[a] = root(father[a]);
        return father[a];
    }
    void insert(int a, int b) {
        // from a to b, so a is b's father
        int root_a = root(a), root_b = root(b);
        father[b] = a;
    }
    bool equal(int a, int b) {
        return root(a) == root(b);
    }
};

class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        UnionSet union_set(n);
        for (int i = 0; i < n; i++) {
            int a = edges[i][0], b = edges[i][1];
            if (union_set.equal(a, b)) {
                return edges[i];
            } else {
                union_set.insert(a, b);
            }
        }
        return vector<int>();
    }
};
