class Solution {
    func findNumberIn2DArray(_ matrix: [[Int]], _ target: Int) -> Bool {
        if matrix == [] || matrix == [[]] { return false }

        let row = matrix.count //行
        let column = matrix[0].count //列

        var index = 0
        while index < row {
            if matrix[index][0] > target {
                index += 1
                continue
            }
            for num in matrix[index] {
                if num == target {
                    return true
                }
                if num > target {
                    break
                }
            }
            index += 1
        }


        return false
    }
}
