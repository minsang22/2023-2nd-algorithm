numTestCases = int(input())

def ReservingString(data, start, end):
    if (start == end or start > end):
        return data
    else :
        data[start], data[end] = data[end], data[start]
        start += 1
        end -= 1
        return ReservingString(data, start, end)
        
for t in range(numTestCases):
    data = str(input())
    data_len = len(data)
    res = []
    ans = ""
    
    for i in range(0, data_len):
        res.append(data[i])
    
    res = ReservingString(res, 0, data_len-1)
    
    for j in range(0, data_len):
        ans += res[j]
        
    print(ans)