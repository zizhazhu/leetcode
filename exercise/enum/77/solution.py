class Solution:
    def combineN(self, n: int, now: int, k: int, nums: List[int], result: List[List[int]]):
        if len(nums) == k:
            result.append(list(nums))
        else:
            for next_num in range(now + 1, n + 1):
                nums.append(next_num)
                self.combineN(n, next_num, k, nums, result)
                nums.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.combineN(n, 0, k, [], result)
        return result
        
