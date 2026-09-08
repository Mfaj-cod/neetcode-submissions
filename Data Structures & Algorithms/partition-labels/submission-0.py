class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        seen = set()
        res, curr = [], []

        def iscomplete(seen: set()) -> bool:
            nonlocal count
            for c in seen:
                if count[c] != 0:
                    return False
            return True

        for i in range(len(s)):
            curr.append(s[i])
            count[s[i]] -= 1
            seen.add(s[i])

            if iscomplete(seen):
                res.append(len(curr))
                curr.clear()
                seen.clear()
        
        return res