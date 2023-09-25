import sys
sys.setrecursionlimit(10**7)
numTestCases = int(input())

def Exponent(x, n):
    if n == 0 :
        return 1
    elif (n % 2 == 1) :
        res = Exponent(x, (n-1)/2)
        return x * res * res % 1000
    else :
        res = Exponent(x,n/2)
        return res * res % 1000

for t in range(numTestCases):
    data = input().split()
    data = list(map(int, data))
    ans = Exponent(data[0], data[1])
    print(ans)