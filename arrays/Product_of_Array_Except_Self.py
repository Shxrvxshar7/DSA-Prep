# Problem: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Approach: Two-Pass

class Solution(object):
    def productExceptSelf(self, nums):
        
        left = [0] *len(nums)
        right = [0] * len(nums)
        left_running = 1
        right_running = 1
        final =[]
        for i in range(len(nums)):
            left[i] = left_running
            left_running = left_running * nums[i]
        for i in range(len(nums)-1,-1,-1):
            right[i]= right_running
            right_running = right_running * nums[i]
        
        for i in range(len(nums)):
            final.append(left[i] * right[i])
        return final
    
""" Time complexity:
    Left array → O(n)
    Right array → O(n)
    Final loop → O(n)
    Total → O(n)"""

 #n + n + n = O(n). That's optimal.
#Space complexity is O(n) because of the left and right arrays.