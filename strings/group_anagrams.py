# Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Approach: Hash Table

class Solution(object):
    def groupAnagrams(self, strs):
        count = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            count[sorted_word] = count.get(sorted_word,[])
            count[sorted_word].append(word)

        return count.values()
            
# Sorting each word → O(m log m) where m = length of the word
#Looping through all words → O(n) where n = number of words
#Total Time Complexity → O(n * m log m)