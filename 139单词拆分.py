#回溯暴搜 36/45 时间复杂度O(2^n)太慢
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def backsearch(s, startindex, path, result):
            if startindex == len(s):
                result.append(list(path))
                return
            for i in range(startindex, len(s)):
                zichuan = s[startindex:i+1]
                if zichuan not in wordDict:
                    continue
                path.append(zichuan)
                backsearch(s, i+1, path, result)
                path.pop()
            return result
        
        res = backsearch(s, 0, [], [])
        if len(res) == 0: 
            return False
        else:
            return True

#动态规划 完全背包 更优
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for j in range(len(s)+1):
            for i in range(j):
                if s[i:j] in wordDict and dp[i] == True:
                    dp[j] = True
        
        return dp[-1]
