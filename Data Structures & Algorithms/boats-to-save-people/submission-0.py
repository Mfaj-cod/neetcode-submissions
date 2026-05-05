class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0

        for i in range(len(people)):
            if people[i] == limit:
                boats += 1
            
            for j in range(i+1, len(people)):
                if people[i] + people[j] == limit:
                    boats += 1
            
        return boats