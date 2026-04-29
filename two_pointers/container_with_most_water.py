# Problem: Container with most water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Approach: Two Pointers


class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) -1 

        max_area = 0

        while l < r:
            width = r -l
            area = width * min(height[l],height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l +=1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return max_area
            

#Time comp = O(n)