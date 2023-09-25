numTestCases = int(input())

def Fibonacci(n):
    if n <= 1 :
        return n
    else :
        return Fibonacci(n-1) + Fibonacci(n-2)

for t in range(numTestCases):
    data = int(input())
    print(Fibonacci(data))