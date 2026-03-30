class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for ele in row:
                if ele != "." and ele in row_set:
                    return False
                elif ele ==".":
                    continue
                row_set.add(ele)
        
        for col_index in range(9):
            col_set = set()
            for row_index in range(9):
                ele = board[row_index][col_index]
                if ele != "." and ele in col_set:
                    return False
                elif ele ==".":
                    continue
                col_set.add(ele)
        
        for i in range(9):
            grid_set = set()
            for row_index in range(3):
                for col_index in range(3):
                    abs_row, abs_col = row_index+(i//3)*3 , col_index+(i%3)*3
                    ele = board[abs_row][abs_col]
                    if ele != "." and ele in grid_set:
                        return False
                    elif ele ==".":
                        continue
                    grid_set.add(ele)
        
        return True



            