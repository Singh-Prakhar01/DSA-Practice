# Last updated: 27/07/2026, 23:30:16
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        min_price = prices[0]
5        ans = 0
6        
7        for i in range (1,n):
8            curr_profit = prices[i]-min_price 
9            ans = max(curr_profit,ans)
10            min_price = min(min_price,prices[i])
11
12        return ans
13
14