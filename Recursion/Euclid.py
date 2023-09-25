import sys
sys.setrecursionlimit(10**7)
numTestCases = int(input())

def gcd(a,b):
    if (b == 0) : 
        return a 
    else :
        return gcd(b, a%b)

for t in range(numTestCases):
    data = input().split()
    data = list(map(int, data))
    ans = gcd(data[0], data[1])
    print(ans)