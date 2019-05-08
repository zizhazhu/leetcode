class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int m = matrix.size();
        if (m == 0) return result;
        int n = matrix[0].size();
        if (n == 0) return result;
        int layer = min(m + 1, n + 1) / 2;
        for (int i = 0; i < layer; i++) {
            if (i == m - i - 1) {
                for (int j = i; j < n - i; j++)
                    result.push_back(matrix[i][j]);
            } else if (i == n - i - 1) {
                for (int j = i; j < m - i; j++)
                    result.push_back(matrix[j][i]);
            } else {
                int begin[4][2] = {{i, i}, {i, n - i - 1}, {m - i - 1, n - i - 1}, {m - i - 1, i}};
                int way[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
                for (int j = 0; j < 4; j++) {
                    for (int x = begin[j][0], y = begin[j][1]; x != begin[(j + 1) & 3][0] || y != begin[(j + 1) & 3][1]; x += way[j][0], y += way[j][1]) {
                        result.push_back(matrix[x][y]);
                    }
                }
            }
        }
        return result;
    }
};
