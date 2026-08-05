class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            if n > 0:
                hashmap[n] = hashmap.get(n, 0) + 1
                
        if hashmap == {}:
            return 1

        maxx = max(nums)
        for i in range(1, maxx+1):
            if i not in hashmap:
                return i
        
        return maxx + 1