# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Approach: Hash Table



class Solution(object):
    def isAnagram(self, s, t):
        count={}
        if len(s) != len(t):
            return False
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            count[ch] = count.get(ch, 0) - 1
        return all(val == 0 for val in count.values())
            
# Time complexity: O(n)