class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = sum(matchsticks) // 4
        sticks = {}
        for m in matchsticks:
            sticks[m] = 1 + sticks.get(m, 0)
        
        visited = set()
        for i in range(len(matchsticks)):
            if i in visited:
                continue

            if matchsticks[i] == side:
                sticks[matchsticks[i]] -= 1
            elif matchsticks[i] < side:
                remaining = side - matchsticks[i]

                if remaining in sticks:
                    sticks[remaining] -= 1
                    sticks[matchsticks[i]] -= 1
            else:
                return False
                
            visited.add(i)
        
        return True