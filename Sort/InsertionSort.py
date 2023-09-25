numTestCases = int(input())

for t in range(numTestCases):
    data = input().split()[1:]
    data = list(map(int, data))
    data_len = len(data)
    swap_cnt = 0
    comp_cnt = 0
        
    for i in range(1, data_len):
        tmp = data[i]
        for j in range(i, 0, -1):
            comp_cnt += 1
            if (data[j] < data[j-1]):
                data[j], data[j-1] = data[j-1], data[j]
                swap_cnt += 1
            else:
                break
                
    print(comp_cnt, swap_cnt)