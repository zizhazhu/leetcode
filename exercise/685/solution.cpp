struct UnionSet {
    vector<int> father;
    UnionSet(): father(1001) {
        for (int i = 0; i < father.size(); i++) father[i] = i;
    }
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
        int result = -1;
        int n = edges.size();
        int redundant_node = -1;
        bool first = false;
        UnionSet union_set;
        for (int i = 0; i < n; i++) {
            int a = edges[i][0], b = edges[i][1];
            if (union_set.root(b) != b) {
                redundant_node = b;
            } else if (union_set.equal(a, b)) {
                if (redundant_node == -1) {
                    first = true;
                    result = i;
                } else {
                    first = true;
                    break;
                }
            } else {
                union_set.insert(a, b);
            }
        }
        if (redundant_node == -1) {
            return edges[result];
        } else {
            for (int i = 0; i < n; i++) {
                if (edges[i][1] == redundant_node) {
                    if (first) return edges[i];
                    else first = true;
                }
            }
        }
        return vector<int>();
    }
};
