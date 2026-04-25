# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Approach: Two Pointers
class Solution(object):
    def maxProfit(self, prices):
        cp = 0
        sp = 1 
        mp = 0

        while sp < len(prices):
            if prices[sp]>prices[cp]:
                profit = prices[sp] - prices[cp]
                if profit > mp:
                    mp = profit
            else:
                cp = sp
            sp += 1

        return mp


# Time complexity: O(n) 