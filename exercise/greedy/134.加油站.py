#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        real_cost = []
        for i in range(len(gas)):
            real_cost.append(gas[i] - cost[i])
        no = 0
        while no < len(gas):
            all_gas = 0
            length = 0
            while length < len(gas):
                next_no = (no + length) % len(gas)
                all_gas += real_cost[next_no]
                if all_gas >= 0:
                    length += 1
                else:
                    break
            if length == len(gas):
                return no
            else:
                no = no + length + 1
        return -1

            
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1])