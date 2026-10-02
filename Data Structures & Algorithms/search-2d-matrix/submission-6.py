class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        if (target < matrix[0][0]) or (target > matrix[m - 1][n - 1]):
            return False

        l, r = 0, m - 1
        target_row = int()
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                target_row = mid
                break

        # now perform binary search on target row
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            mid_num = matrix[target_row][mid]

            if target < mid_num:
                r = mid - 1
            elif target > mid_num:
                l = mid + 1
            else:
                return True
        
        return False
            
