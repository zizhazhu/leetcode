#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        edges = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            pre, now = prerequisite
            edges[now].append(pre)

        node_status = {}

        def dfs(s, begin):
            for next in edges[s]:
                if next not in node_status:
                    node_status[next] = 1
                    if not dfs(next, begin):
                        return False
                    node_status[next] = 2
                elif node_status[next] == 1:
                    return False
            return True

        for i in range(numCourses):
            if i in node_status:
                continue
            node_status[i] = 1
            if not dfs(i, i):
                return False
            node_status[i] = 2
        return True
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])