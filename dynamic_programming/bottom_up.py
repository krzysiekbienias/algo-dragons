from typing import List
import math

# 120 Triangle - leetcode - medium
def minimum_total(triangle: List[List[int]]) -> int:
        n=len(triangle)
        m=len(triangle[-1])
        dp=[[0]*i for i in range(1,n+1)]
        dp[0][0]=triangle[0][0]
        for row in range(1,n):
            for col in range(row+1):
                min_above=math.inf
                if col==0: #we are on the left there is only one cell above with location (r-1,col)
                    min_above=dp[row-1][col]
                    dp[row][col]=min_above+triangle[row][col]
                elif col==row: #we are in the right edge so we might move from this location (r-1,col-1)
                    min_above=dp[row-1][col-1]
                    dp[row][col]=min_above+triangle[row][col]
                else:
                    min_above=min(dp[row-1][col-1],dp[row-1][col])
                    dp[row][col]=min_above+triangle[row][col]
        return min(dp[n-1])
                    
                       
                    
                

print(minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]]))
print('the end')