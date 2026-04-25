# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Approach: HashMap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
# Time complexity: O(n)