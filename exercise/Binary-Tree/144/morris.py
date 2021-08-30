# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        p = root
        while p:
            if p.left is None:
                result.append(p.val)
                p = p.right
            else:
                pre = p.left
                while pre.right and pre.right != p:
                    pre = pre.right
                if pre.right == p:
                    pre.right = None
                    p = p.right
                else:
                    pre.right = p
                    result.append(p.val)
                    p = p.left
        return result

