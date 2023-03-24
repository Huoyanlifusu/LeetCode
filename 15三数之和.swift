class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let len = nums.count
        if len < 3 { return [] }
        var lst = nums
        lst = lst.sorted()
        var ans = [[Int]]()
        for i in 0..<len {
            if lst[i] > 0 { return ans }
            if i > 0 && lst[i] == lst[i-1] {
                continue
            }
            var left = i + 1
            var right = len - 1
            while left < right {
                if lst[left] + lst[right] + lst[i] == 0 {
                    ans.append([lst[i], lst[left], lst[right]])
                    while left < len - 1 && lst[left] == lst[left + 1] {
                        left += 1
                    }
                    while right > 0 && lst[right] == lst[right - 1] {
                        right -= 1
                    }
                    left += 1
                    right -= 1
                } else if lst[left] + lst[right] + lst[i] > 0 {
                    right -= 1
                } else {
                    left += 1
                }
            }
        }
        return ans
    }
}
