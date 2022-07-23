class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        else:
            return maxP
                
            