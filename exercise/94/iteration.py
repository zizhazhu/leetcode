# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        p = root
        while p or len(stack) > 0:
            if p is None:
                p = stack.pop()
                result.append(p.val)
                p = p.right
            else:
                while p:
                    stack.append(p)
                    p = p.left
        return result
