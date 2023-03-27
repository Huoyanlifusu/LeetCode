class Solution {
    func isValid(_ s: String) -> Bool {
        if s.count % 2 == 1 { return false }
        let dic = ["{":"}",
                "(":")",
                "[":"]"]
        let chars = Array(s)
        var stack = [String]()
        for char in chars {
            if dic[String(char)] != nil {
                stack.append(String(char))
            } else {
                if stack.isEmpty || dic[stack[stack.count - 1]] != String(char) {
                    return false
                }
                stack.popLast()
            }
        }
        return stack.isEmpty
    }
}
