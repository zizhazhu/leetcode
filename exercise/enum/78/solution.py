class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        now = set()
        n = len(nums)

        def subsetsN(index):
            if index == n:
                result.append(list(now))
            else:
                subsetsN(index + 1)
                now.add(nums[index])
                subsetsN(index + 1)
                now.remove(nums[index])

        subsetsN(0)
        return result
