class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        def dfs(i, j, k):
            if not 0 <= i < row or not 0 <= j < col or not board[i][j] == word[k]:
                return False
            if k == len(word) - 1:
                return True 
            board[i][j] = ''
            res = dfs(i - 1, j, k + 1) or dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = word[k]
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False
