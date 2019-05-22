class Solution:
    def permuteUniquePart(self, nums, result, reached, now):
        if len(now) == len(nums):
            result.append(list(now))
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not reached[i-1]:
                    continue
                reached[i] = True
                now.append(nums[i])
                self.permuteUniquePart(nums, result, reached, now)
                now.pop()
                reached[i] = False

    def permuteUnique(self, nums):
        result = []
        now = []
        nums.sort()
        reached = [False for _ in range(len(nums))]
        self.permuteUniquePart(nums, result, reached, now)
        return result
