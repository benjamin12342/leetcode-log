#虽然一眼看出解法，但是moveCost的数组比较奇怪，入门略高一点点难度
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        

        
        m,n = len(grid),len(grid[0])
        dp = [[10**9 for _ in range (n)] for _ in range(m)]
        dp[0][:] = grid[0][:]
#dp [i][j] = max(dp[i][j] , max(dp[i-1][j]+cost[]))
        minCost = 10**9
        for i in range(1,m):
            for j in range(0,n):
                for k in range(0,n):
                    dp[i][j]= min(dp[i][j],grid[i][j]+dp[i-1][k]+moveCost[grid[i-1][k]][j])
                    if i==m-1 :
                        minCost = min(dp[i][j],minCost)
        return minCost