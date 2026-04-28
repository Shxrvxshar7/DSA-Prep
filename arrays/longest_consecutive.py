# Problem: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Approach: Hash Set

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num-1) not in num_set:
                length = 1
                while(num + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest



        
# Time complexity: O(n)