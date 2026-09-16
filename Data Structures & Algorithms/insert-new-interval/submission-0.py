class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, inter in enumerate(intervals):
            st, end = inter

            if st > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append([st, end])
            else:
                newInterval = [min(newInterval[0], st), max(newInterval[1], end)]
        
        res.append(newInterval)
        return res
            