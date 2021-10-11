class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        unsigned m = grid.size();
        if (m == 0) return 0;
        unsigned n = grid[0].size();
        if (n == 0) return 0;
        vector<int> f(n);
        f[0] = grid[0][0];
        for (int i = 1; i < n; i++) {
            f[i] = f[i-1] + grid[0][i];
        }
        for (int i = 1; i < m; i++) {
            f[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                f[j] = min(f[j], f[j-1]) + grid[i][j];
            }
        }
        return f[n-1];
    }
};
