class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1 # left: buy, right: sell
        n = len(prices)

        while r < n and l < n:
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                l = r
            r += 1
        
        return max_profit