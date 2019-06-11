class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        unsigned m = obstacleGrid.size();
        if (m == 0) return 0;
        unsigned n = obstacleGrid[0].size();
        if (n == 0) return 0;
        if (obstacleGrid[0][0] == 1 || obstacleGrid[m-1][n-1] == 1)
            return 0;
        vector<int> counts(n, 0);
        for (unsigned i = 0; i < m; i++) {
            if (obstacleGrid[i][0] == 1) counts[0] = 0;
            for (unsigned j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1) counts[j] = 0;
                else counts[j] += counts[j-1];
            }
        }
        return counts[n-1];
    }
};
