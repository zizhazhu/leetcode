class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            order = ''.join(sorted(s))
            if order in result:
                result[order].append(s)
            else:
                result[order] = [s]
        output = []
        for k, v in result.items():
            output.append(v)
        return output

