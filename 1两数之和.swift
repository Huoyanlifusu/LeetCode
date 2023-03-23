class Solution {

    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var hashTable = [Int: Int]()
        
        for i in 0..<nums.count {
            if hashTable.keys.contains(target - nums[i]) && i != hashTable[target-nums[i]]! {
                return [i, hashTable[target-nums[i]]!]
            }
            if !hashTable.keys.contains(nums[i]) {
                hashTable[nums[i]] = i
            }
        }
        return [-1, -1]
    }
}
