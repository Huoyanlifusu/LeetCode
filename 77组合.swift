class Solution {
    var path = [Int]()
    var array = [[Int]]()

    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        backSearch(n, k, 1)
        return array
    }

    func backSearch(_ n: Int, _ k: Int, _ startIndex: Int) {
        if k == 0 {
            array.append(path)
            return
        }
        if startIndex > n { return }
        for i in startIndex...n {
            path.append(i)
            backSearch(n, k-1, i+1)
            path.removeLast()
        }
    }
}
