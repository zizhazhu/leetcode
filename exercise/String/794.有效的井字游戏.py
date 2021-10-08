#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#

# @lc code=start
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_X, count_O = 0, 0
        for s in board:
            for c in s:
                if c == 'X':
                    count_X += 1
                if c == 'O':
                    count_O += 1

        def win(player):
            for s in board:
                if s[0] == s[1] == s[2] == player:
                    return True
            for i in range(3):
                if board[0][i] == board[1][i] == board[2][i] == player:
                    return True
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[2][0] == board[1][1] == board[0][2] == player:
                return True
        
        win_X = win("X")
        win_O = win("O")

        if win_X and not win_O and count_X == count_O + 1:
            return True
        if win_O and not win_X and count_O == count_X:
            return True
        if not win_X and not win_O and (count_X == count_O or count_X == count_O + 1):
            return True

        return False
# @lc code=end

