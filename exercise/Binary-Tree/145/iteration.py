# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [(root, 0)]
        while len(stack) > 0:
            now = stack.pop()
            if now[0] is None:
                continue
            if now[1] == 0:
                stack.append((now[0], 1))
                stack.append((now[0].right, 0))
                stack.append((now[0].left, 0))
            else:
                result.append(now[0].val)
        return result
