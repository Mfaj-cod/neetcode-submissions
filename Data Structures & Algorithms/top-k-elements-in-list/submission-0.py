class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        s_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        
        res = []
        for key in s_hashmap:
            if k != 0:
                res.append(key)
            else:
                return res
            k -= 1
        
        return res