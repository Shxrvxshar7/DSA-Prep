# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Easy
# Approach: Two Pointers


class Solution(object):
    def twoSum(self, numbers, target):
        l = 0 
        r = len(numbers)-1
        num = 0
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -=1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]
        
# Time complexity: O(n)