class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r, d = deque(), deque()
        
        for i, s in enumerate(senate):
            r.append(i) if s == "R" else d.append(i)
        
        while r and d:
            dturn = d.popleft()
            rturn = r.popleft()

            if rturn < dturn:
                r.append(dturn + len(senate))
            else:
                d.append(rturn + len(senate))

        return "Radiant" if r else "Dire"
