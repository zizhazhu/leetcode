class Graph {
    vector<unordered_map<int, int>> edges;
public:
    Graph(int n): edges(n + 1) {}

    void insert(int from, int to, int time) {
        edges[from][to] = time;
    }

    int dijkstra(int s) {
        vector<int> dis(edges.size(), 1000000);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> queue;
        unordered_set<int> reached;
        queue.push(make_pair(0, s));
        dis[s] = 0;
        while (!queue.empty()) {
            pair<int, int> now = queue.top();
            queue.pop();
            if (reached.count(now.second) != 0)
                continue;
            reached.insert(now.second);
            for (const pair<int, int> &it: edges[now.second]) {
                if (dis[it.first] > dis[now.second] + it.second) {
                    dis[it.first] = dis[now.second] + it.second;
                    queue.push(make_pair(dis[it.first], it.first));
                }
            }
        }
        int result = 0;
        for (int i = 1; i < edges.size(); i++) {
            if (dis[i] == 1000000) {
                return -1;
            } else if (dis[i] > result) {
                result = dis[i];
            }
        }
        return result;
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
