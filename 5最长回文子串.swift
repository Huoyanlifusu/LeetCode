    func longestPalindrome(_ s: String) -> String {
        if s.count <= 1 { return s}
        let chars = Array(s)
        var maxInterval = 0
        var ans = String(chars[0])
        for i in 0..<chars.count {
            let intervalA = check(chars, i - 1, i + 1)
            let intervalB = check(chars, i, i + 1)
            maxInterval = max(intervalA, intervalB, maxInterval)
            if maxInterval == intervalA {
                ans = String(chars[i-intervalA/2...i+intervalA/2])
            }
            if maxInterval == intervalB {
                ans = String(chars[i-intervalB/2...i+1+intervalB/2])
            }
        }
        return ans
    }

    func check(_ chars: [String.Element], _ left: Int, _ right: Int) -> Int {
        var left = left, right = right
        while left >= 0 && right < chars.count {
            if chars[left] != chars[right] {
                break
            }
            left -= 1
            right += 1
        }
        return right - left - 2
    }
