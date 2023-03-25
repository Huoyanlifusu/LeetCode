class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        let len = nums.count
        if len == 1 { return [nums[0]*nums[0]]}
        var left = 0
        var right = len - 1
        var lst = nums
        var j = len - 1
        while j >= 0 {
            let rPow = nums[right] * nums[right]
            let lPow = nums[left] * nums[left]
            if rPow > lPow {
                lst[j] = rPow
                j -= 1
                right -= 1
            } else if lPow >= rPow {
                lst[j] = lPow
                j -= 1
                left += 1
            }
        }
        return lst
    }
}
