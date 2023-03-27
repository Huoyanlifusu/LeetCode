class MyQueue {
    var queue: [Int]?

    init() {
        queue = [Int]()
    }
    
    func push(_ x: Int) {
        queue?.append(x)
    }
    
    func pop() -> Int {
        return queue!.removeFirst()
    }
    
    func peek() -> Int {
        return queue![0]
    }
    
    func empty() -> Bool {
        return queue!.isEmpty
    }
}
