#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        result = Node(node.val, None)

        node_queue = deque()
        node_queue.append((node, result))
        node_pool = {
            result.val: result,
        }

        while node_queue:
            source, target = node_queue.popleft()
            for n in source.neighbors:
                if n.val in node_pool:
                    target.neighbors.append(node_pool[n.val])
                else:
                    t = Node(n.val, None)
                    node_pool[n.val] = t
                    target.neighbors.append(t)
                    node_queue.append((n, t))
        
        return result
        
# @lc code=end

