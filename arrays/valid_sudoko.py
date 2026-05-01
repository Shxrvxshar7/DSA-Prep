# Problem: Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/
# Difficulty: Medium
# Approach: HashMap


import collections
class Solution(object):
    def isValidSudoku(self, board):
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        s = collections.defaultdict(set)
        
        for row in range(len(board)):
            for column in range(len(board)):    
                
                if board[row][column] ==".":
                    continue 
                                    
                value = board[row][column]
                
                if value in r[row] or value in c[column] or value in s[row//3,column//3]:
                    return False
                
                r[row].add(value)
                c[column].add(value)
                s[row//3,column//3].add(value)
                
        return True

""" Time complexity: O(1) because the board is always 9x9.""" 
                            

        