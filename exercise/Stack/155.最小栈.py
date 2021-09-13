#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._mins = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._mins) == 0:
            self._mins.append(0)
        else:
            if val < self._stack[self._mins[-1]]:
                self._mins.append(len(self._stack) - 1)
            else:
                self._mins.append(self._mins[-1])


    def pop(self) -> None:
        self._stack.pop()
        self._mins.pop()


    def top(self) -> int:
        return self._stack[-1]


    def getMin(self) -> int:
        return self._stack[self._mins[-1]]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

