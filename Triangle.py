class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]  # копія останнього рядка

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
        
triangle = [[2],
            [3,4],
            [6,5,7],
            [4,1,8,3]]

s = Solution()
print(s.minimumTotal(triangle))