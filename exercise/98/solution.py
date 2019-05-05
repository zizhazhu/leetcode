# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        last = 0
        valid = False
        now = root
        while now:
            if not now.left:
                if not valid or last < now.val:
                    last = now.val
                    valid = True
                else:
                    return False
                now = now.right
                continue
            pre = now.left
            while pre.right and pre.right == now:
                pre = pre.right
            if not pre.right:
                pre.right = now
                now = now.left
            else:
                pre.right = None
                if not valid or last < now.val:
                    last = now.val
                    valid = True
                else:
                    return False
                now = now.right
        return True
