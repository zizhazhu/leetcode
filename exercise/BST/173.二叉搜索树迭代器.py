#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path = []
        now = root
        while now:
            self.path.append(now)
            now = now.left
        self.begin = True


    def next(self) -> int:
        if self.begin:
            self.begin = False
        else:
            now = self.path.pop()
            if now.right:
                n = now.right
                while n:
                    self.path.append(n)
                    n = n.left
        return self.path[-1].val


    def hasNext(self) -> bool:
        if len(self.path) == 0:
            return False
        elif len(self.path) == 1:
            if self.begin == True or self.path[-1].right:
                return True
            else:
                return False
        else:
            return True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

