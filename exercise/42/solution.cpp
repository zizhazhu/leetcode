class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> left(n), right(n);
        int Max = 0;
        for (int i = 0; i < n; i++) {
            left[i] = Max;
            if (height[i] > Max) Max = height[i];
        }
        Max = 0;
        for (int i = n - 1; i >= 0; i--) {
            right[i] = Max;
            if (height[i] > Max) Max = height[i];
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            int Min = min(left[i], right[i]);
            if (Min > height[i])
                result += Min - height[i];
        }
        return result;
    }
};
