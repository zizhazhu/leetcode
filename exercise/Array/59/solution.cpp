class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result(n, vector<int>(n));
        int way[][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int now = 1, index_x = 0, index_y = 0, direction = 0;
        int all = n * n;
        while (now <= all) {
            result[index_x][index_y] = now;
            int next_x = index_x + way[direction][0], next_y = index_y + way[direction][1];
            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= n || result[next_x][next_y] != 0) {
                direction = (direction + 1) % 4;
                next_x = index_x + way[direction][0];
                next_y = index_y + way[direction][1];
            }
            index_x = next_x, index_y = next_y;
            now++;
        }
        return result;
    }
};
