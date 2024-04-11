#
from typing import List
class Solution:
     def countPairs(self, nums: List[int], target: int) -> int:
          l = len(nums)
          n=0
          for i in range(l-1):
               for j in range(i+1,l):
                    if nums[i]+nums[j]<target:
                         n+=1     
          
          return n
     

solution  = Solution()
#print(solution.countPairs([1,2,3,4,5],5))

nums = list(map(int, input().split()))
target = int(input)