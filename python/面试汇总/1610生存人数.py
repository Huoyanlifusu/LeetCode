class Solution(object):
    def maxAliveYear(self, birth, death):
        """
        :type birth: List[int]
        :type death: List[int]
        :rtype: int
        """
        cnt = [0] * 102
        n = len(birth)
        for i in range(n):
            cnt[birth[i]-1900] += 1
            cnt[death[i]-1900+1] -= 1
        
        tmp = 0
        ans = [-float("inf"), 0]
        for i in range(102):
            tmp += cnt[i]
            if tmp > ans[0]:
                ans = [tmp, i+1900]
        return ans[1]