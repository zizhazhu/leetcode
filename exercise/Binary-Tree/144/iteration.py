# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]
        while len(stack) > 0:
            now = stack.pop()
            if now is not None:
                result.append(now.val)
                stack.append(now.right)
                stack.append(now.left)
        return result
