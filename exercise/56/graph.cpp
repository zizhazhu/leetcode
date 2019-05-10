class Graph {
public:
    vector<unordered_set<int>> edges;
    Graph(int n): edges(n) {}
    void add(int a, int b) {
        edges[a].insert(b);
        edges[b].insert(a);
    }

};

class Solution {
public:
    void dfs(Graph &g, vector<bool> &reached, int v, vector<int> &now, const vector<vector<int>> &intervals) {
        for (const int &t: g.edges[v]) {
            if (!reached[t]) {
                if (intervals[t][0] < now[0]) now[0] = intervals[t][0];
                if (intervals[t][1] > now[1]) now[1] = intervals[t][1];
                reached[t] = true;
                dfs(g, reached, t, now, intervals);
            }
        }
    }

    vector<vector<int>> travel(Graph &g, int n, const vector<vector<int>> &intervals) {
        vector<vector<int>> result;
        vector<bool> reached(n);
        for (int i = 0; i < n; i++) {
            if (!reached[i]) {
                vector<int> now;
                reached[i] = true;
                now.push_back(intervals[i][0]);
                now.push_back(intervals[i][1]);
                dfs(g, reached, i, now, intervals);
                result.push_back(now);
            }
        }
        return result;
    }

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        Graph g(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (intervals[i][0] <= intervals[j][1] && intervals[i][0] >= intervals[j][0])
                    g.add(i, j);
            }
        }
        return travel(g, intervals.size(), intervals);
    }
};

