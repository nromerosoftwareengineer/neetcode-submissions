class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        if len(prices) <= 1:
            return 0 


        l = 0
        r = l + 1

        while  r < len(prices):
            print("maxProfit: " + str(maxProfit))
            print("l "+ str(l))
            print("r "+ str(r))
            print("(prices[r] - prices[l])" + str((prices[r] - prices[l])))
            if maxProfit < (prices[r] - prices[l]):
                maxProfit = max(maxProfit, (prices[r] - prices[l]))
                r = r + 1
            else:
                if prices[r] < prices[l]:
                    l = r
                r = r + 1 
      
                


           
            
            

        return maxProfit 

        