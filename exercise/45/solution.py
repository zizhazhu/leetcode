class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        edge = 0
        steps = [0 for _ in range(len(nums))] 
        for i in range(len(nums)):
            if i + nums[i] >= len(nums) - 1:
                return steps[i] + 1
            elif i + nums[i] > edge:
                for j in range(edge + 1, i + nums[i] + 1):
                    steps[j] = steps[i] + 1
                edge = i + nums[i]
        return steps[-1]
