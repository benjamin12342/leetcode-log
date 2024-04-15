#可能是dp,没想明白解法
from typing import List

import math


class Solution:
 
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1


        while (height[i+1]>=height[i]and i + 1 < j):
                i+=1
        
        while(i!=j):
             height1 = height[i]
             if(height[i+1])
       

        water = 0  
        

        # while (i < j - 1 ):
        #     while (height[i+1]>=height[i]and i + 1 < j):
        #         i+=1
        
        #     while (height[j-1]>=height[j]and i < j - 1):
        #         j-=1
            
        #     if(b):
        #         water -= (j-i-1)* min(hight2,hight1)
        #     else:
        #         b = 1
        #     hight1 = height[i]
        #     hight2 = height[j]
        #     water += (j-i-1)* min(hight2,hight1)
        #     while(height[i+1]<= hight1 and i + 1< j):
        #         water -= min(hight1,hight2,height[i+1])
        #         i+=1

        #     while(height[j-1] <= hight2 and i < j -1 ):
        #         water -= min(hight1,hight2,height[j-1])
        #         j -= 1

        return water

        
        
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height)) 