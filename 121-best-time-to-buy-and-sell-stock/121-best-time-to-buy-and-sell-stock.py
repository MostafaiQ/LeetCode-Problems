class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            numL = prices[l]
            numR = prices[r]
            profit = numR - numL
            if numL < numR:
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        else:
            return maxP
                
            