# Problem: Search 2d Matrix
# Link: https://leetcode.com/problems/searcjh_2d_matrix/
# Difficulty: Medium
# Approach: Two pointers


class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
    

Time Comp: O log M*N