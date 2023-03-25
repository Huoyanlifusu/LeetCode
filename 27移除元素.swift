class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        let len = nums.count
        var j = 0
        for i in 0..<len {
            if nums[i] != val {
                nums[j] = nums[i]
                j += 1
            }
        }
        return j
    }
}
