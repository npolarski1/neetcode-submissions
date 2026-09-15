class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # init row hashsets
        row_sets = [set() for _ in range(9)]
        # init col hashsets
        col_sets = [set() for _ in range(9)]
        # init sub-box hashsets
        box_map = {(x, y): set() for x in range(0, 3) for y in range (0, 3)}

        # loop over board
        for r_i, r in enumerate(board):
            # loop over row
            for c_i, n in enumerate(r):
                if n == ".":
                    continue
                # if current num is in current row hashset return false
                # check col hashset too
                if n in row_sets[r_i] or n in col_sets[c_i]:
                    return False
                # check sub-box hashset
                if n in box_map[(r_i // 3, c_i // 3)]:
                    return False

                row_sets[r_i].add(n)
                col_sets[c_i].add(n)
                box_map[(r_i // 3, c_i // 3)].add(n)
                
        # return true if whole loop goes through
        return True
