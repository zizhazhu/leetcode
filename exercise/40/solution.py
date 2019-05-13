class Solution:
    def combinationSum2Part(self, candidates, target, index, result, now):
        if target == 0:
            result.append(list(now))
        elif index >= len(candidates) or candidates[index] > target:
            return
        else:
            now.append(candidates[index])
            self.combinationSum2Part(candidates, target - candidates[index], index + 1, result, now)
            now.pop()
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[next_index-1]:
                next_index += 1
            self.combinationSum2Part(candidates, target, next_index, result, now)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        now = []
        self.combinationSum2Part(candidates, target, 0, result, now)
        return result

