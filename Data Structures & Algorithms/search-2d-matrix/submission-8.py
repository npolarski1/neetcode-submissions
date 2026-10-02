class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        if (target < matrix[0][0]) or (target > matrix[m - 1][n - 1]):
            return False

        l, r = 0, m - 1
        target_row = -1

        while l <= r:
            mid = (l + r) // 2

            if target_row >= 0: # row has been found, we're searching row
                mid_num = matrix[target_row][mid]
                if target < mid_num:
                    r = mid - 1
                elif target > mid_num:
                    l = mid + 1
                else:
                    return True
            else: # row hasn't been found yet, we're searching matrix
                if target < matrix[mid][0]:
                    r = mid - 1
                elif target > matrix[mid][-1]:
                    l = mid + 1
                else:
                    target_row = mid

                    # set left of search window to first of target row
                    # set right to last
                    l, r = 0, n - 1
        
        return False

        # time: O(log(m * n))
        # space: O(1)
            
