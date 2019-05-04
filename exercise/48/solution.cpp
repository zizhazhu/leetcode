class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // from outer layer to inner layer
        for (int i = 0; i < n / 2; i++) {
            int start = i, end = n - i - 1;
            for (int j = start; j < end; j++) {
                int x = i, y = j;
                int t = matrix[x][y];
                matrix[x][y] = matrix[n-1-y][x];
                matrix[n-1-y][x] = matrix[n-1-x][n-1-y];
                matrix[n-1-x][n-1-y] = matrix[y][n-1-x];
                matrix[y][n-1-x] = t;
            }
        }
    }
};
