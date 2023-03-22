class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        if nums == [] { return -1 }
        if target == nums[0] { return 0 }
        var left = 0
        var right = nums.count-1
        
        while left <= right {
            let mid = (left + right)/2
            if nums[mid] == target {
                return mid
            }
            if target > nums[0] {
                if nums[mid] > target {
                    right = mid - 1
                } else if target > nums[mid] {
                    if nums[mid] < nums[0] {
                        right = mid - 1
                    } else {
                        left = mid + 1
                    }
                }
            } else if target < nums[0] {
                if nums[mid] < target {
                    left = mid + 1
                } else {
                    if nums[mid] >= nums[0] {
                        left = mid + 1
                    } else {
                        right = mid - 1
                    }
                }
            }
        }
        return -1
    }
}
