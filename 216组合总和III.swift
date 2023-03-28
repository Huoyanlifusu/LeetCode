class Solution {
    var array = [[Int]]()
    var path = [Int]()
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        backSearch(k, 0, 1, n)
        return array
    }
    // k - 当前层数, n - 当前总和
    func backSearch(_ k: Int, _ n: Int, _ startIndex: Int, _ target: Int) {
        if k == 0 {
            if n == target {
                array.append(path)
            }
            return
        }
        if startIndex > 9 { return }
        for i in startIndex...9 {
            path.append(i)
            backSearch(k-1, n+i, i+1, target)
            path.removeLast()
        }
    }
}
