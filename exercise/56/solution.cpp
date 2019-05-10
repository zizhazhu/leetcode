struct {
    bool operator()(vector<int> *a, vector<int> *b) const {
        return (*a)[0] < (*b)[0];
    }
} customLess;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        vector<vector<int>*> intervals_ref;
        for (int i = 0; i < intervals.size(); i++) {
            intervals_ref.push_back(&intervals[i]);
        }
        sort(intervals_ref.begin(), intervals_ref.end(), customLess);
        vector<int> now;
        for (int i = 0; i < intervals_ref.size(); i++) {
            if (now.empty()) now = *intervals_ref[i];
            else {
                if ((*intervals_ref[i])[0] > now[1]) {
                    result.push_back(now);
                    now = *intervals_ref[i];
                } else {
                    now[1] = max((*intervals_ref[i])[1], now[1]);
                }
            }
        }
        if (!now.empty()) result.push_back(now);
        return result;
    }
};
