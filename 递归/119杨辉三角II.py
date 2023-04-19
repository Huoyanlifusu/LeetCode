class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def digui(num, path):
            if num == 1:
                return path
            tmp = [1]
            for i in range(len(path)-1):
                tmp.append(path[i]+path[i+1])
            tmp.append(1)
            path = digui(num-1, tmp)
            return path
        
        if rowIndex == 0:
            return [1]
        else:
            return digui(rowIndex, [1,1])
