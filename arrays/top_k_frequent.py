# Problem: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Approach: Hash Table

class Solution(object):
    def topKFrequent(self, nums, k):
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_pairs = sorted(count.items(), key = lambda x :x[1], reverse = True)
        output = []
        for i in range(k):
            output.append(sorted_pairs[i][0])
        return output
            
        
""" Time complexity:
    Frequency count → O(n)
    Sorting → O(n log n)
    Final loop → O(k)
    Total → O(n log n)"""