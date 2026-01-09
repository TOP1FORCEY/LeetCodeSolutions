class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        bp = [0] * (n + 1)
        bp[0] = bp[1] = 0
        
        for i in range(2, n + 1):
            bp[i] = min(bp[i - 1] + cost[i - 1], bp[i - 2] + cost[i - 2])

        return bp[n]
            


cost = [10,15,20]

s = Solution()
print(s.minCostClimbingStairs(cost))