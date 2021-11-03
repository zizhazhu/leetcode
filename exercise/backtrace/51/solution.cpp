class Solution {
public:
    void findNQueens(vector<vector<string>> &result, vector<int> &axis, unordered_set<int> &col, unordered_set<int> &left_up, unordered_set<int> &left_down, int n) {
        if (axis.size() == n) {
            vector<string> solution;
            for (int i = 0; i < axis.size(); i++) {
                string line;
                for (int j = 0; j < axis[i]; j++) line.push_back('.');
                line.push_back('Q');
                while (line.length() < n) line.push_back('.');
                solution.push_back(line);
            }
            result.push_back(solution);
        }
        int x = axis.size();
        for (int i = 0; i < n; i++) {
            if (col.find(i) == col.end() && \
                    left_up.find(x-i) == left_up.end() && \
                    left_down.find(x+i) == left_down.end()) {
                axis.push_back(i);
                col.insert(i);
                left_up.insert(x-i);
                left_down.insert(x+i);
                findNQueens(result, axis, col, left_up, left_down, n);
                col.erase(i);
                left_up.erase(x-i);
                left_down.erase(x+i);
                axis.pop_back();
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<int> axis;
        unordered_set<int> col, left_up, left_down;
        findNQueens(result, axis, col, left_up, left_down, n);
        return result;
    }
};
