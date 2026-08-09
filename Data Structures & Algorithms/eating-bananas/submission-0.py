class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = 1
        while True:
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / rate)
            
            if totalTime <= h:
                return rate
            rate += 1
        
        return speed