//滑动窗口
class Solution {
    func minSubArrayLen(_ target: Int, _ nums: [Int]) -> Int {
        let len = nums.count
        if len == 1 {
            if nums[0] == target { return 1 }
            else { return 0 }
        }
        var left = 0, right = 0, sum = 0
        var ans = 0
        while right < len {
            sum += nums[right]
            while sum >= target {
                if ans == 0 {
                    ans = right - left + 1
                } else {
                    ans = min(ans, right-left+1)
                }
                sum -= nums[left]
                left += 1
            }
            right += 1
        }

        return ans
    }
}
