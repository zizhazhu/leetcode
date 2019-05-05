# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBSTEdge(self, root: TreeNode, left: int, right: int) -> bool:
        if root is None:
            return True
        if left is not None and left >= root.val:
            return False
        if right is not None and right <= root.val:
            return False
        left_valid = self.isValidBSTEdge(root.left, left, root.val)
        right_valid = self.isValidBSTEdge(root.right, root.val, right)
        return left_valid and right_valid

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTEdge(root, None, None)
