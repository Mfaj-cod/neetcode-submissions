class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i: int, curr: List[int], total: int) -> None:
            if target == total:
                res.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return

            # include candidates[i]
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            
            # don't include candidates[i]
            curr.pop()

            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res

