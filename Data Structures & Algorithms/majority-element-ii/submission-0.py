class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = dict()
        for e in nums:
            hashmap[e] = hashmap.get(e, 0) + 1
        
        res = []
        for key, val in hashmap.items():
            if val > n/3:
                res.append(key)

        return res