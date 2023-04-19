class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def digui(row, path, res):
            if row == 2:
                return res
            tmp = [1]
            for i in range(len(path)-1):
                tmp.append(path[i]+path[i+1])
            tmp.append(1)
            res.append(tmp)
            res = digui(row-1, tmp, res)
            return res
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            return digui(numRows, [1,1], [[1],[1,1]])
