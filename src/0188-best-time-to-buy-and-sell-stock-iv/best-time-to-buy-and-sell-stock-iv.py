# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete at most k transactions.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#  
# Example 1:
#
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
#
#
# Example 2:
#
#
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#
#
#  
# Constraints:
#
#
# 	1 <= k <= 100
# 	1 <= prices.length <= 1000
# 	0 <= prices[i] <= 1000
#
#


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k == 0: return 0
        
        delta = [prices[i+1]-prices[i] for i in range (len(prices)-1)]
        B=[sum(delta) for _, delta in groupby(delta, key=lambda x: x < 0)]
        n = len(B) + 1
        
        if k > len(prices) // 2: return sum(x for x in B if x > 0)
        
        dp = [[0]*(k+1) for _ in range(n-1)] 
        mp = [[0]*(k+1) for _ in range(n-1)]
        
        dp[0][1], mp[0][1] = B[0], B[0]
        
        for i in range(1, n-1):
            for j in range(1, k+1):
                dp[i][j] = max(mp[i-1][j-1], dp[i-1][j]) + B[i]
                mp[i][j] = max(dp[i][j], mp[i-1][j])

        return max(mp[-1])
    
