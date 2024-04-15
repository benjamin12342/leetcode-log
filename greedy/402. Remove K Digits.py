#贪心算法，去除k个位数找最小数，思路很不清晰，细节处理很差
class Solution2:
#暴力失败
   
    def __init__(self):
        self.ans = -1
    def string_to_int(self,num: str, matrix:str) -> int :
        ans  = 0
        for i in range(len(num)):
            if matrix[i] == 1:
                continue
            else :
                ans = ans * 10 + int(num[i])
        
        return ans

        
    def check(self,i, num, k, ki,matrix) :
        if(ki <= k) and (self.ans == -1 or self.ans > self.string_to_int(num,matrix)) :
            self.ans = self.string_to_int(num, matrix)
        if ki>k or i>= len(num):
            return
        

        

        ki+=1
        matrix[i] = 1
        self.check(i+1,num, k,ki,matrix)
        matrix[i] = 0
        ki -= 1
        self.check(i+1,num, k, ki,matrix)
        
        


         
            
    
    def removeKdigits(self, num: str, k: int) -> str:
        matrix = [0 for i in range(len(num))]


        self.check (0,num,k,0,matrix)
        matrix[0] = 1
        self.check (0,num,k,1,matrix)
        
       

        return str(self.ans)
    
class Solution():
   
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack=[]
        
        for i in range(len(num)):
            if k == 0 or len(stack) == 0:
                if not (num[i]== '0' and len(stack) == 0):
                    stack.append(num[i])
                continue
            
            else:
                while(len(stack) > 0 and num[i]< stack[-1]  and k > 0):
                    
                    k -= 1
                    stack.pop()
                    
            if not (num[i]== '0' and len(stack) == 0):
                stack.append(num[i])
        while(k > 0):
            k -= 1
            if not (len(stack) == 0):
                stack.pop()
        if len(stack) == 0:
            return '0'

        return ''.join(stack)    

            


num = "10"
k = 2
sou = Solution()
print(sou.removeKdigits(num,k) )