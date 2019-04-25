class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> row[9], col[9], block[9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                int block_no = i / 3 * 3 + j / 3;
                if (row[i].find(c) != row[i].end() || col[j].find(c) != col[j].end() || block[block_no].find(c) != block[block_no].end())
                    return false;
                row[i].insert(c);
                col[j].insert(c);
                block[block_no].insert(c);
            }
        }
        return true;
    }
};
