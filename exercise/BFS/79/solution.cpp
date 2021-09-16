class Solution {
public:
    int ways[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    bool inBoard(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }

    bool DFS(int x, int y, vector<vector<char>> &board, vector<vector<bool>> &reached, string &now, const string &word) {
        if (now.length() == word.length())
            return now == word;
        int index = now.length();
        for (int i = 0; i < 4; i++) {
            int new_x = x + ways[i][0], new_y = y + ways[i][1];
            if (inBoard(new_x, new_y, board.size(), board[0].size()) && !reached[new_x][new_y] && board[new_x][new_y] == word[index]) {
                reached[new_x][new_y] = true;
                now.push_back(word[index]);
                if (DFS(new_x, new_y, board, reached, now, word))
                    return true;
                now.pop_back();
                reached[new_x][new_y] = false;
            }
        }
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        if (m == 0) {
            return false;
        }
        int n = board[0].size();
        if (n == 0) {
            return false;
        }
        vector<vector<bool>> reached(m, vector<bool>(n, false));
        string now;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    reached[i][j] = true;
                    now.push_back(word[0]);
                    if (DFS(i, j, board, reached, now, word)) {
                        return true;
                    }
                    now.pop_back();
                    reached[i][j] = false;
                }
            }
        }
        return false;
    }
};
