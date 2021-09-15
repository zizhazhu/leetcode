#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 1
        now = root
        while now.left:
            now = now.left
            level += 1
        left = 2 ** (level - 1)
        right = 2 ** level - 1
        
        def exist(num):
            mask = 1 << (level - 2)
            now = root
            while mask:
                if (mask & num) == 0:
                    now = now.left
                else:
                    now = now.right
                mask >>= 1
            return now is not None

        while left < right:
            mid = (left + right) // 2 + 1
            if exist(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
            
# @lc code=end