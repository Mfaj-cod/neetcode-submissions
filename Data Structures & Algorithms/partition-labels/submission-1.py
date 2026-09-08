class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {} # c -> last i in s
        for i, c in enumerate(s):
            last_ind[c] = i
        
        res = []
        curr_size, curr_end = 0, 0
        for i, c in enumerate(s):
            curr_size += 1
            curr_end = max(curr_end, last_ind[c])

            if i == curr_end:
                res.append(curr_size)
                curr_size = 0
        
        return res