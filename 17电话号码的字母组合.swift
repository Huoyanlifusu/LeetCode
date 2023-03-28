class Solution {
    var array = [String]()
    var cur_str = [String]()
    let dic = ["2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]]
    func letterCombinations(_ digits: String) -> [String] {
        if digits == "" { return [] }
        let count = digits.count
        let chars = Array(digits)
        backSearch(count, count, chars, &cur_str)
        return array
    }

    func backSearch(_ k: Int,_ n: Int, _ digits: [String.Element], _ currentStr: inout [String]) {
        if k == 0 {
            array.append(currentStr.joined())
            return
        }
        for char in dic[String(digits[n-k])]! {
            currentStr.append(char)
            backSearch(k-1, n, digits, &currentStr)
            currentStr.removeLast()
        }
    }
}
