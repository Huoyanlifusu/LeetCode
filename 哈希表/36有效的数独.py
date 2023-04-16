class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dic_col = {}
            dic_row = {}
            dic_box = {}
            for j in range(9):
                if board[i][j] in dic_row or board[j][i] in dic_col or board[3*(i//3)+j//3][3*(i%3)+j%3] in dic_box:
                    return False
                if board[i][j] != ".":
                    dic_row[board[i][j]] = 1
                if board[j][i] != ".":
                    dic_col[board[j][i]] = 1
                if board[3*(i//3)+j//3][3*(i%3)+j%3] != ".":
                    dic_box[board[3*(i//3)+j//3][3*(i%3)+j%3]] = 1
        return True
