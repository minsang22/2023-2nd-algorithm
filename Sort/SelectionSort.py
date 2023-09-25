numTestCases = int(input())

for t in range(numTestCases):
    data = input().split()[1:]
    data = list(map(int, data))
    data_len = len(data)
    swap_cnt = 0
    comp_cnt = 0
    for i in range(data_len - 1):
        data_min = i
        for j in range(i+1, data_len):
            comp_cnt += 1
            if (data[j] < data[data_min]):
                data_min = j
        
        if (data_min != i):
            swap_cnt += 1
            data[data_min], data[i] = data[i], data[data_min]
            
    print(comp_cnt, swap_cnt)