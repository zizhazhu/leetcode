class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxarea = 0, left = 0, right = height.size() - 1;
        while (left < right) {
            int area = (right - left) * min(height[left], height[right]);
            if (area > maxarea) {
                maxarea = area;
            }
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxarea;
    }
};
