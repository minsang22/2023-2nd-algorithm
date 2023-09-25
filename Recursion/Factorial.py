import sys
sys.setrecursionlimit(10**7)
numTestCases = int(input())

def Factorial(n):
    if n == 0 :
        return 1
    else :
        return n * Factorial(n-1)

for t in range(numTestCases):
    data = int(input())
    res = str(Factorial(data))
    res_len = len(res)
    
    for i in range(res_len - 1, -1, -1):
        if res[i] != str(0):
            tmp = i
            break
    
    if res_len < 4:
        print(res[0:tmp+1])
    else:
        if res_len == tmp+1 :
            print(res[res_len-3:])
        else:
            print(res[tmp-2:tmp+1])