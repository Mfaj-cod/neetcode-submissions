class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        k = 0
        for key, val in hashmap.items():
            nums[k] = key
            k += 1
        
        return k
