class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            length = right - left
            edge = min(height[left], height[right])
            area = length * edge
            if result < area:
                result = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
