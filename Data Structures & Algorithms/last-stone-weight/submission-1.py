class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        left = 0
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] != stones[-2]:
                y = stones.pop()
                stones[-1] = abs(y - stones[-1])
                stones.sort()
            else:
                if stones:
                    left = stones[0]
        
        return left + 1