class Graph {
    vector<unordered_map<int, int>> edges;
public:
    Graph(int n): edges(n + 1) {}

    void insert(int from, int to, int time) {
        edges[from][to] = time;
    }

    int dijkstra(int s) {
        vector<int> result(edges.size());
        priority_queue<pair<int, int>> queue;
        unordered_set<int> reached;
        queue.push(make_pair(0, s));
        for (int i = 1; i < edges.size(); i++) {
            if (i != s) {
                queue.push(make_pair(-1000000, i));
            }
        }
        while (!queue.empty()) {
            pair<int, int> now = queue.top();
            queue.pop();
            if (reached.count(now.second) != 0)
                continue;
            result[now.second] = now.first;
            reached.insert(now.second);
            for (const pair<int, int> &it: edges[now.second]) {
                if (reached.count(it.first) != 0)
                    continue;
                else
                    queue.push(make_pair(-(-now.first + it.second), it.first));
            }
        }
        int sum = 0;
        for (int i = 1; i < result.size(); i++)
            sum += result[i];
        return sum;
    }
};

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        Graph g(N);
        for (int i = 0; i < times.size(); i++) {
            g.insert(times[i][0], times[i][1], times[i][2]);
        }
        return g.dijkstra(K);
    }
};
