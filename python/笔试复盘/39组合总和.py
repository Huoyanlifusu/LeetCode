class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        ans = []
        candidates.sort()
        def dfs(total, pre):
          if total == target:
            ans.append(list(path))
            return
          elif total > target:
            return
          elif total + pre > target:
            return
          for x in candidates:
            if x >= pre:
              pre = x
              path.append(x)
              dfs(total+x, pre)
              path.pop()
        
        dfs(0, 0)
        return ans
