# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        result = []
        queue = deque()
        queue.append((root, 0))
        now_level = 0
        now = []
        while len(queue) > 0:
            node = queue.popleft()
            if node[0]:
                if node[1] > now_level:
                    result.append(now)
                    now = []
                now.append(node[0].val)
                queue.append(node[0].left)
                queue.append(node[0].right)
        if len(now) > 0:
            result.append(now)
        return result
