class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(i: int, currentList: List[int], total: int):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.add(tuple(currentList.copy()))
            
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])

            currentList.pop()
            dfs(i + 1, currentList, total)
        
        dfs(0, [], 0)
        return [ list(t) for t in res ]