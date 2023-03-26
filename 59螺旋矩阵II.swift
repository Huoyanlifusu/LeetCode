class Solution {
    func generateMatrix(_ n: Int) -> [[Int]] {
        var mat = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        
        var t = 0, b = n - 1, l = 0, r = n - 1
        var num = 1, total = n * n
        while num <= total {
            for i in l...r {
                mat[t][i] = num
                num += 1
            }
            if num > total { break }
            t += 1
            for i in t...b {
                mat[i][r] = num
                num += 1
            }
            if num > total { break }
            r -= 1
            for i in stride(from: r, to: l-1, by: -1) {
                mat[b][i] = num
                num += 1
            }
            if num > total { break }
            b -= 1
            for i in stride(from: b, to: t-1, by: -1) {
                mat[i][l] = num
                num += 1
            }
            l += 1
        }
        
        return mat
    }
}
