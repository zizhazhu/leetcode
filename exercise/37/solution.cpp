class Solution {
public:
    bool check(vector<unordered_set<int>> &row, vector<unordered_set<int>> &col, vector<unordered_set<int>> &block, int i, int j, int d) {
        int b_i = i / 3, b_j = j / 3;
        if (row[i].find(d) != row[i].end()) return false;
        if (col[j].find(d) != col[j].end()) return false;
        if (block[b_i * 3 + b_j].find(d) != block[b_i * 3 + b_j].end()) return false;
        return true;
    }

    bool solve(vector<vector<char>>& board, int i, int j, vector<unordered_set<int>> &row, vector<unordered_set<int>> &col, vector<unordered_set<int>> &block) {
        if (i == 9) return true;
        if (j == 9) return solve(board, i + 1, 0, row, col, block);
        if (board[i][j] != '.') return solve(board, i, j + 1, row, col, block);
        for (int d = 1; d <= 9; d++) {
            if (check(row, col, block, i, j, d)) {
                board[i][j] = d + '0';
                row[i].insert(d);
                col[j].insert(d);
                block[i / 3 * 3 + j / 3].insert(d);
                if (solve(board, i, j + 1, row, col, block)) return true;
                board[i][j] = '.';
                row[i].erase(d);
                col[j].erase(d);
                block[i / 3 * 3 + j / 3].erase(d);
            }
        }
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        vector<unordered_set<int>> row(9), col(9), block(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    row[i].insert(board[i][j] - '0');
                    col[j].insert(board[i][j] - '0');
                    block[i / 3 * 3 + j / 3].insert(board[i][j] - '0');
                }
            }
        }
        
        solve(board, 0, 0, row, col, block);
    }
};
