class Solution {
    var result = [[Int]]()
    var res = [Int]()
    var numbers = [Int]()
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {
        numbers = [Int](repeating: 0, count: candidates.count)
        backSearch(candidates.sorted(), target, 0, 0)
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
            if (index > 0 && candidates[index-1] == candidates[index] && numbers[index-1] == 0) {
                continue
            }
            numbers[index] = 1
            res.append(candidates[index])
            backSearch(candidates, target, sum+candidates[index], index+1)
            res.popLast()
            numbers[index] = 0
        }
    }
}
