# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def update(self, root: TreeNode, last:TreeNode, first: TreeNode, second: TreeNode) -> bool:
        if last and root.val < last.val:
            if first:
                second = root
                return True
            else:
                first, second = last, root
        last = root
        return False

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        last = None
        first, second = None, None
        while root:
            if root.left is None:
                if self.update(root, last, first, second):
                    break
                root = root.right
                continue
            pre = root.left
            while pre.right and pre.right != root:
                pre = pre.right
            if pre.right:
                pre.right = None
                if self.update(root, last, first, second):
                    break
                root = root.right
            else:
                pre.right = root
                root = root.left
        first.val, second.val = second.val, first.val

