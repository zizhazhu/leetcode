class Solution:
    def combinationSumPart(self, candidates, target, index, result, now):
        if target == 0:
            result.append(list(now))
        else:
            if index == len(candidates) or candidates[index] > target:
                return
            now.append(candidates[index])
            self.combinationSumPart(candidates, target - candidates[index], index, result, now)
            now.pop()
            self.combinationSumPart(candidates, target, index+1, result, now)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        now = []
        self.combinationSumPart(candidates, target, 0, result, now)
        return result

