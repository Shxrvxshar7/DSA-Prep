# Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Approach: Two Pointers


class Solution(object):
    def isPalindrome(self, s):
        s = [char.lower() for char in s if char.isalnum()]
        l = 0
        r = len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# Time complexity: O(n) 