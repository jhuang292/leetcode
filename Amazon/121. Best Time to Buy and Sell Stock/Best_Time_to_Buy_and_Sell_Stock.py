class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_day = 0
        maxProfit = 0
        
        for i in range(len(prices)):
            if(prices[i] < prices[buy_day]):
                buy_day = i
                
            maxProfit = max(maxProfit, prices[i] - prices[buy_day])
        return maxProfit
            
        
