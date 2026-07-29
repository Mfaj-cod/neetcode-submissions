class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = defaultdict(int)

        for ppl, trst in trust:
            trustMap[ppl] -= 1
            trustMap[trst] += 1
        
        for i in range(1, n+1):
            if trustMap[i] == n-1:
                return i
                
        return -1