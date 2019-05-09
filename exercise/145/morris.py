# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def reverseResult(self, result, begin, end):
        for i in range((end - begin) // 2):
            result[begin+i], result[end-1-i] = result[end-i-1], result[begin+i]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        p = root
        while p:
            if p.left is None:
                p = p.right
            else:
                pre = p.left
                while pre.right and pre.right != p:
                    pre = pre.right
                if pre.right == p:
                    pre.right = None
                    now = len(result)
                    output_p = p.left
                    while output_p != pre:
                        result.append(output_p.val)
                        output_p = output_p.right
                    result.append(pre.val)
                    self.reverseResult(result, now, len(result))
                p = p.right
                else:
                    pre.right = p
                    p = p.left
        return result

