class Solution {
    func isInterleave(_ s1: String, _ s2: String, _ s3: String) -> Bool {
        let rowNum = s1.count
        let colNum = s2.count
        let totalNum = s3.count
        
        if rowNum + colNum != totalNum { return false }
        
        var boolMat = [[Bool]](repeating: [Bool](repeating: false, count: colNum+1), count: rowNum+1)
        boolMat[0][0] = true
        
        for i in 0..<rowNum+1 {
            for j in 0..<colNum+1 {
                if i >= 1 && s1[s1.index(s1.startIndex, offsetBy: i-1)] == s3[s3.index(s3.startIndex, offsetBy: i+j-1)] {
                    boolMat[i][j] = boolMat[i][j] || boolMat[i-1][j]
                }
                if j >= 1 && s2[s2.index(s2.startIndex, offsetBy: j-1)] == s3[s3.index(s3.startIndex, offsetBy: i+j-1)] {
                    boolMat[i][j] = boolMat[i][j-1] || boolMat[i][j]
                }
            }
        }
        
        return boolMat[rowNum][colNum]
    }

    
}
