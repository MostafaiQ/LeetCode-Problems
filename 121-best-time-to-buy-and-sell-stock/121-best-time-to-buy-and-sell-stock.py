# Greedy Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyStock = float('inf')
        finalAnswer = 0
        for currentStock in prices:
            buyStock = min(buyStock, currentStock)
            finalAnswer = max(finalAnswer, currentStock - buyStock)
        return finalAnswer
                
            