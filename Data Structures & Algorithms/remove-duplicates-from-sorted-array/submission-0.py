class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        i = 0
        for key, val in hashmap.items():
            nums[i] = key
            i += 1
        
        return i
