class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        set<int> full;
        for (int i = 1; i <= 9; i++)
            full.insert(i);
        vector<set<int>> row(9, set(full)), col(9, set(full)), block(9, set(full));
        vector<vector<bool>> filled(9, vector<bool>(9, false));
        int filled_count = 0;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    row[i].erase(board[i][j] - '0');
                    col[j].erase(board[i][j] - '0');
                    block[i / 3 * 3 + j / 3].erase(board[i][j] - '0');
                    filled[i][j] = true;
                    filled_count++;
                }
            }
        }
        vector<vector<set<int>>> point(9, vector<set<int>>(9, set<int>()));
        priority_queue<pair<int, pair<int, int>>> to_solve;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (!filled[i][j]) {
                    set<int> temp;
                    set_intersection(row[i].begin(), row[i].end(), col[j].begin(), col[j].end(), inserter(temp, temp.begin()));
                    set_intersection(temp.begin(), temp.end(), block[i / 3 * 3 + j / 3].begin(), block[i / 3 * 3 + j / 3].end(), inserter(point[i][j], point[i][j].begin()));
                    to_solve.push(make_pair(-point[i][j].size(), make_pair(i, j)));
                }
            }
        }
        while (filled_count < 81) {
            pair<int, pair<int, int>> p = to_solve.top();
            to_solve.pop();
            int x = p.second.first, y = p.second.second;
            int value = *point[x][y].begin();
            cout << value << ' ' << x << ' ' << y << endl;
            board[x][y] = value + '0';
            filled[x][y] = true;
            filled_count++;
            set<pair<int, int>> reached;
            reached.insert(make_pair(x, y));
            for (int i = 0; i < 9; i++) {
                if (!filled[x][i]) {
                    point[x][i].erase(value);
                    if (reached.find(make_pair(x, i)) != reached.end()) {
                        reached.insert(make_pair(x, i));
                        to_solve.push(make_pair(-point[x][i].size(), make_pair(x, i)));
                    }
                }
                if (!filled[i][y]) {
                    point[i][y].erase(value);
                    if (reached.find(make_pair(i, y)) != reached.end()) {
                        reached.insert(make_pair(i, y));
                        to_solve.push(make_pair(-point[i][y].size(), make_pair(i, y)));
                    }
                }
                int a = x / 3 * 3 + i / 3, b = y / 3 * 3 + i % 3;
                if (!filled[a][b]) {
                    point[a][b].erase(value);
                    if (reached.find(make_pair(a, b)) != reached.end()) {
                        reached.insert(make_pair(a, b));
                        to_solve.push(make_pair(-point[a][b].size(), make_pair(a, b)));
                    }
                }
            }
        }
    }
};
