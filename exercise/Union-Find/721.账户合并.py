#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#

# @lc code=start
class Solution:
    def __init__(self):
        self.root = {}
        self.email_mapping = {}
        self.email_reverse = {}

    def findRoot(self, a):
        if a not in self.root:
            self.root[a] = a
        if self.root[a] != a:
            self.root[a] =  self.findRoot(self.root[a])
        return self.root[a]


    def merge(self, a, b):
        a_root = self.findRoot(a)
        b_root = self.findRoot(b)
        if a_root == b_root:
            return
        else:
            self.root[b_root] = a_root

    def email_to_no(self, email):
        if email in self.email_mapping:
            return self.email_mapping[email]
        else:
            no = len(self.email_mapping)
            self.email_mapping[email] = no
            self.email_reverse[no] = email
            return no
            

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        name_mapping = {}
        for account in accounts:
            name = account[0]
            first_no = self.email_to_no(account[1])
            for i in range(1, len(account)):
                name_mapping[account[i]] = name
                self.merge(self.email_to_no(account[i]), first_no)
        result_map = {}
        for email_no in self.root.keys():
            root_no = self.findRoot(email_no)
            email = self.email_reverse[email_no]
            root = self.email_reverse[root_no]
            if root in result_map:
                result_map[root].append(email)
            else:
                result_map[root] = [email]
        results = []
        for key, value in result_map.items():
            value.sort()
            name = name_mapping[key]
            result = list()
            result.append(name)
            result.extend(value)
            results.append(result)
        return results
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])