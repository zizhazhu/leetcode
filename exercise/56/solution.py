class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) == 0:
            return result
        intervals_sorted = sorted(intervals)
        begin, end = -1, -1
        for interval in intervals_sorted:
            if interval[0] > end:
                if end >= 0:
                    result.append([begin, end])
                begin, end = interval[0], interval[1]
            else:
                end = max(end, interval[1])
        result.append([begin, end])
        return result
