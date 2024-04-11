#简单的数组加减数学问题。定义了输入输出，处理方式有进步空间，能否单独通过input，output而不用字符串分割呢？
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
          times = 0
          
          for i in range(len(tickets)):
               if k>=i :
                    times += min(tickets[i], tickets[k])
               else:
                    times += min(tickets[i], tickets[k] - 1)
               
          
          return times
    #tickets = [5,1,1,1], k = 0
def parse_input(input_string):
     tickets_string = input_string.split(']')[0].split('[')[1].strip()
     tickets = list(map(int, tickets_string.split(',')))
     k_str =  input_string.split('],')[1].split('=')[1].strip()
     k = int(k_str)
     return tickets, k
input_string = input()
tickets, k = parse_input(input_string)
sol = Solution()
print ("",sol.timeRequiredToBuy(tickets, k))