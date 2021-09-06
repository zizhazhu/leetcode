# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        last = None
        first, second = None, None

        def update() -> bool:
            nonlocal last, first, second
            return False

        while root:
            if root.left is None:
                if last and root.val < last.val:
                    if first is None:
                        first = last
                    second = root
                last = root
                root = root.right
                continue
            pre = root.left
            while pre.right and pre.right != root:
                pre = pre.right
            if pre.right:
                pre.right = None
                if last and root.val < last.val:
                    if first is None:
                        first = last
                    second = root
                last = root
                root = root.right
            else:
                pre.right = root
                root = root.left
        first.val, second.val = second.val, first.val

