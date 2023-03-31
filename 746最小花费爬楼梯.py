class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0,0]
        for i in range(2, len(cost)+1):
            mincost.append(min(mincost[i-1]+cost[i-1], mincost[i-2]+cost[i-2]))
        return mincost[-1]
