# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [(root, 0)]
        while len(stack) > 0:
            p = stack.pop()
            if p[0] is None:
                continue
            if p[1] == 0:
                stack.append((p[0].right, 0))
                stack.append((p[0], 1))
                stack.append((p[0].left, 0))
            else:
                result.append(p[0].val)
        return result

