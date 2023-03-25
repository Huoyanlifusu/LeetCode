class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        if nums == [] { return -1 }
        if nums.count == 1 {
            if target == nums[0] {
                return 0
            } else {
                return -1
            }
        }
        
        var left = 0
        var right = nums.count - 1
        while left <= right {
            let mid = (left + right)/2
            if target == nums[mid] {
                return mid
            } else if target > nums[mid] {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return -1
    }
}
