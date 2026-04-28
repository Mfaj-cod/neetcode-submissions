class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = dict()
        res, maxCount = 0, 0

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            res = n if hashmap[n] > maxCount else res
            maxCount = max(hashmap[n], maxCount)

        return res