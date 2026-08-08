class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sideL = sum(matchsticks) // 4
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != sideL:
            return False
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= sideL:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False

        return backtrack(0)