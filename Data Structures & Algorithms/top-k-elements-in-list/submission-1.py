class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        # s_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        
        # res = []
        # for key in s_hashmap:
        #     if k != 0:
        #         res.append(key)
        #     else:
        #         return res
        #     k -= 1
        
        # return res

        freq = [[] for i in range(len(nums)+1)]

        for n, c in hashmap.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

