#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def isValid(addr):
            for num in addr:
                if num[0] == "0" and num != "0":
                    return False
                if int(num) > 255:
                    return False
            return True
        
        results = []
        addr = []
        def dfs(now):
            if len(addr) == 4:
                if now == len(s) and isValid(addr):
                    results.append('.'.join(addr))
            else:
                for i in range(now + 1, min(len(s) + 1, now + 4)):
                    addr.append(s[now:i])
                    dfs(i)
                    addr.pop()
        dfs(0)
        return results

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.restoreIpAddresses("25525511152")
