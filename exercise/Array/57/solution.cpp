class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int state = 0;
        int begin = newInterval[0];
        for (int i = 0; i < intervals.size(); i++) {
            switch (state) {
                case 0:
                    if (intervals[i][1] < newInterval[0]) {
                        result.push_back(intervals[i]);
                    }
                    else if (intervals[i][0] < newInterval[0]) {
                        begin = intervals[i][0];
                        state = 1;
                    }
                    else {
                        begin = newInterval[0];
                        state = 1;
                    }
                case 1:
                    if (intervals[i][0] > newInterval[1]) {
                        result.push_back({begin, newInterval[1]});
                        result.push_back(intervals[i]);
                        state = 2;
                    } else if (intervals[i][1] < newInterval[1]) {
                        continue;
                    } else {
                        result.push_back({begin, intervals[i][1]});
                        state = 2;
                    }
                    break;
                case 2:
                    result.push_back(intervals[i]);
            }
        }
        if (state == 0 || state == 1) result.push_back({begin, newInterval[1]});
        return result;
    }
};
