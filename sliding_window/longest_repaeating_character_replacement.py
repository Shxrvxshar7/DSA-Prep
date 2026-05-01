# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Medium
# Approach: HashTable



class Solution(object):
    def characterReplacement(self, s, k):
        max_freq = 0
        count = {}
        l = 0
        r = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


#Time Comp: O(n)