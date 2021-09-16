class Node:

    def __init__(self, init, now: tuple):
        self.all_str = set(init)
        self.now = now


class Solution:

    way = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def exist(self, board: List[List[str]], word: str) -> bool:
        import queue
        q = queue.Queue()
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    q.put(Node([(i, j)], (i, j)))
        while q.qsize() > 0:
            now = q.get()
            now_axis = now.now
            for i in range(len(self.way)):
                next_axis = (now.now[0] + self.way[i][0], now.now[1] + self.way[i][1])
                if next_axis[0] >= 0 and next_axis[0] < m and next_axis[1] >= 0 and next_axis[1] < n and next_axis not in now.all_str:
                    if word[len(now.all_str)] == board[next_axis[0]][next_axis[1]]:
                        if len(now.all_str) == len(word) - 1:
                            return True
                        new_set = set(now.all_str)
                        new_set.add(next_axis)
                        node = Node(new_set, next_axis)
                        q.put(node)
        return False
