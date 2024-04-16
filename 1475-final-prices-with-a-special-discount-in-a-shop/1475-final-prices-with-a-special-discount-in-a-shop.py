class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)-1):
            j= i+1
            while j<len(prices) and prices[i] - prices[j] < 0 :
                j+=1
                if j == len(prices):
                    return prices
            prices[i] = prices[i] - prices[j]
        return prices 
            
        