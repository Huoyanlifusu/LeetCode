class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        if nums == [] { return [-1, -1] }
        if target > nums[nums.count-1] || target < nums[0] { return [-1, -1] }
        let lm = leftMarginSearch(nums, target)
        let rm = rightMariginSearch(nums, target)
        return [lm, rm]
    }

    func leftMarginSearch(_ nums:[Int], _ target: Int) -> Int {
        var lm = Int.min
        var left = 0
        var right = nums.count-1
        while left <= right {
            let mid = left + (right - left)/2
            if target > nums[mid] {
                left = mid + 1
            } else if target < nums[mid] {
                right = mid - 1
            } else {
                lm = mid
                right -= 1
            }
        }
        if lm != Int.min {
            return lm
        }
        return -1
    }

    func rightMariginSearch(_ nums: [Int], _ target: Int) -> Int {
        var rm: Int = Int.max
        var left = 0
        var right = nums.count-1
        
        while left <= right {
            let mid = left + (right - left)/2
            if target > nums[mid] {
                left = mid + 1
            } else if target < nums[mid] {
                right = mid - 1
            } else {
                rm = mid
                left += 1
            }
        }
        if rm != Int.max {
            return rm
        }
        return -1
    }
}
