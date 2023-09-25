import sys
sys.setrecursionlimit(10**7)
numTestCases = int(input())

def multiply(a, b):
    res = [[0,0],[0,0]]
    res[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000
    res[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000
    res[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000
    res[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000
    return res

def pow(matrix, n):
    if (n == 0 or n == 1) :
        return matrix
    elif n % 2 != 0:
        return multiply(matrix, pow(matrix, n-1))
    else:
        tmp = pow(matrix, n//2)
        return multiply(tmp, tmp)
    
def FastFibonacci(n):
    matrix = [[1,1], [1,0]]
    if n < 2 :
        return n
    else :
        res = pow(matrix, n-1)
        return res[0][0]

for t in range(numTestCases):
    data = int(input())
    ans = FastFibonacci(data) % 1000
    print(ans)