class Solution:
    def combinationSumPart(self, candidates, target, index, result, now):
        if target == 0:
            result.append(now)
        else:
            if index == len(candidates) or candidates[index] > target:
                return
            now.append(candidates[index])
            self.combinationSumPart(candidates, target - candidates[index], index + 1, result, now)
            now.pop()
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[next_index-1]:
                next_index += 1
            self.combinationSumPart(candidates, target, next_index, result, now)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        now = []
        self.combinationSumPart(candidates, target, 0, result, now)
        return result

