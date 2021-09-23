class Solution {
public:
    int m, n;
    void noTo2D(int index, int &x, int &y) {
        x = index / n;
        y = index % n;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        m = matrix.size();
        if (m == 0)
            return false;
        n = matrix[0].size();
        if (n == 0)
            return false;
        int left = 0, right = m * n;
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            int x, y;
            noTo2D(mid, x, y);
            if (matrix[x][y] == target) {
                return true;
            } else if (matrix[x][y] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return false;
    }
};
