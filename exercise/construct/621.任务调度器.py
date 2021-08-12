#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = {}
        all_counter = 0
        for task in tasks:
            if task in task_counter:
                task_counter[task] += 1
            else:
                task_counter[task] = 1
            all_counter += 1
        max_counter, max_num = 0, 0
        for task, c in task_counter.items():
            if c > max_counter:
                max_num = 1
                max_counter = c
            elif c == max_counter:
                max_num += 1
        return max(all_counter, (max_counter - 1) * (n + 1) + max_num)

            
# @lc code=end
