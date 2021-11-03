#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = list(map(int, version1.split('.')))
        version2_list = list(map(int, version2.split('.')))
        if len(version1_list) < len(version2_list):
            version1_list.extend([0] * (len(version2_list) - len(version1_list)))
        if len(version2_list) < len(version1_list):
            version2_list.extend([0] * (len(version1_list) - len(version2_list)))
        for i in range(len(version1_list)):
            if version1_list[i] > version2_list[i]:
                return 1
            elif version1_list[i] < version2_list[i]:
                return -1
        return 0
# @lc code=end

