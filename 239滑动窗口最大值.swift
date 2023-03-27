//单调队列
class Solution {
    func maxSlidingWindow(_ nums: [Int], _ k: Int) -> [Int] {
        let count = nums.count
        if count <= k { return [nums.max()!] }
        
        var queue = [Int]()
        var stack = [Int]()
        for i in 0..<k {
            push(&queue, nums[i])
        }
        stack.append(queue[0])
        for i in k..<count {
            if nums[i-k] == queue[0] {
                queue.removeFirst()
            }
            push(&queue, nums[i])
            stack.append(queue[0])
        }
        return stack
    }

    func push(_ queue: inout [Int], _ num: Int) {
        while queue.last != nil && queue.last! < num {
            queue.popLast()
        }
        queue.append(num)
    }
}
