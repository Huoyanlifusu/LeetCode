class Solution {
    func findNthDigit(_ n: Int) -> Int {
        if n>=0 && n<=9 {
            return n
        }
        var i = 1
        var k = Decimal(10)
        while Decimal(n) >= k {
            i += 1
            k += Decimal(i) * pow(10, i-1) * Decimal(9)
        }
        k -= Decimal(i) * pow(10, i-1) * Decimal(9)
        let intK = Int(NSDecimalNumber(decimal: k).doubleValue) //代表数字
        let res = pow(10, i-1) + (Decimal(n) - k)/Decimal(i)
        let num = Int(NSDecimalNumber(decimal: res).doubleValue)
        let index = (n - intK)%i //代表第几个num
        let char = String(num)[String(num).index(String(num).startIndex, offsetBy: index)]
        
        return Int(String(char))!
    }
}
