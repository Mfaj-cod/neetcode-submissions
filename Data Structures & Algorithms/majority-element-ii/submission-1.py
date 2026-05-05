class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)

        for el in nums:
            hashmap[el] += 1

            if len(hashmap) <= 2:
                continue

            new_hashmap = defaultdict(int)
            for n, c in hashmap.items():
                if c > 1:
                    new_hashmap[n] = c - 1

            hashmap = new_hashmap

        res = []
        for n in hashmap:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res

                
        