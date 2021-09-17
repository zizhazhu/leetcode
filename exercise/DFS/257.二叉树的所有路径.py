#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        results = []
        if root is None:
            return results
        path = []

        def dfs(node):
            if node is None:
                return node
            if node.left is None and node.right is None:
                result = ""
                for n in path:
                    result += str(n.val) + "->"
                result += str(node.val)
                results.append(result)
            else:
                path.append(node)
                dfs(node.left)
                dfs(node.right)
                path.pop()

        dfs(root)
        return results
# @lc code=end

