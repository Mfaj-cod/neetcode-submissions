class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = dict()
        n = len(nums)

        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        for i in range(n):
            if hashmap[nums[i]] > (n/2):
                return nums[i]
        
        return