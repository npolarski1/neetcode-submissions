class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # init max profit to 0
        max_profit = 0
        # init left pointer to 0
        # init right poitner to 1
        l, r = 0, 1

        # while r in bounds
        while r < len(prices):
            # calculate profit and update max
            max_profit = max(max_profit, prices[r] - prices[l])

            # if l price > r price and l < r
            if prices[l] > prices[r] and l < r:
                # move l
                l += 1
            # else
            else:
                # move r
                r += 1
        
        # return max profit
        return max_profit
