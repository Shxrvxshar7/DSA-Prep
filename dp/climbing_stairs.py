# Problem: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: easy
# Approach: Dynamic programming

class Solution(object):
    def climbStairs(self, n):
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
    
#time: O(n)