class Solution {
    var result = [[Int]]()
    var res = [Int]()
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        backSearch(candidates, target, 0, 0)
        return result
    }

    func backSearch(_ candidates: [Int], _ target: Int, _ sum: Int, _ startIndex: Int) {
        if sum > target {
            return
        }
        if sum == target {
            result.append(res)
            return
        }
        if startIndex >= candidates.count {
            return
        }
        for index in startIndex..<candidates.count {
            res.append(candidates[index])
            backSearch(candidates, target, sum+candidates[index], index)
            res.popLast()
        }
    }
}
