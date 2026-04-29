# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/
# Difficulty: Medium
# Approach: Two Pointers

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        final = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            l = i + 1
            r = len(nums) -1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    final.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1  
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return final
                

# Time complexity: O(n^2) because of the nested loop. The sorting step is O(n log n) but the nested loop dominates the time complexity. This is the best 