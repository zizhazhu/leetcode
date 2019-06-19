class NumArray:

    def _update(self, i, val):
        i += self.size - 1
        self._nums[i] = val
        while i != 0:
            i = (i - 1) >> 1
            self._nums[i] = self._nums[(i << 1) + 1] + self._nums[(i << 1) + 2]

    def _sumRange(self, i, j, left, right, index):
        if i <= left and j >= right:
            return self._nums[index]
        if j < left or i > right:
            return 0
        else:
            mid = (left + right) >> 1
            sum_left = self._sumRange(i, j, left, mid, (index << 1) + 1)
            sum_right = self._sumRange(i, j, mid + 1, right, (index << 1) + 2)
            return sum_left + sum_right

    def __init__(self, nums: List[int]):
        self.size = 1
        while self.size < len(nums):
            self.size <<= 1
        self._size = self.size * 2 - 1
        self._nums = [0 for _ in range(self._size)]
        for i in range(len(nums)):
            self._update(i, nums[i])

    def update(self, i: int, val: int) -> None:
        self._update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self._sumRange(i, j, 0, self.size - 1, 0)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
