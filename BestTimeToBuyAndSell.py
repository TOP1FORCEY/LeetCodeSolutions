class Solution(object):
    def maxProfit(self, prices = list):
        
        best = 0
        
        for day, price in enumerate(prices):
            for sell in prices[day:]:
                best = max(best, sell - price)
                
        return best
            
        
prices = [7,2,5,1,6,4]

s = Solution()
print(s.maxProfit(prices))