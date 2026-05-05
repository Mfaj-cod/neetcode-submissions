class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting algorithm for O(1) space
        if not nums:
            return []

        # Find potential candidates
        cand1, cand2, count1, count2 = None, None, 0, 0
        
        for n in nums:
            if cand1 == n:
                count1 += 1
            elif cand2 == n:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates (Required for > n/3 version)
        res = []
        n_third = len(nums) // 3
        for c in [cand1, cand2]:
            if c is not None and nums.count(c) > n_third:
                res.append(c)
                
        return res


                
        