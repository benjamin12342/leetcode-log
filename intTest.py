inputStr  =   input()
inputStr  = inputStr.strip('[]')
#strip默认移除开头结尾空格换行符等
print(inputStr)
inputStr=[int (x) for x in inputStr.split(",")]
print(inputStr)
for i in range(len(inputStr)):
     print (inputStr[i])