#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        for t, f in prerequisites:
            graph[f].append(t)

        result = []
        complete_time = 0

        def DFS(v):
            nonlocal complete_time
            for next in graph[v]:
                if reached[next] == 1:
                    return False
                elif reached[next] == 2:
                    continue
                reached[next] = 1
                if not DFS(next):
                    return False
                reached[next] = 2
                result.append((complete_time, next))
                complete_time += 1
            return True

        reached = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if reached[i] == 0:
                reached[i] = 1
                if not DFS(i):
                    return []
                reached[i] = 2
                result.append((complete_time, i))
                complete_time += 1
        
        result.sort(reverse=True)
        order = []
        for t, no in result:
            order.append(no)
        return order
# @lc code=end

s = Solution()
print(s.findOrder(2, [[1, 0]]))
