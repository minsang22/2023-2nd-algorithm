numTestCases = int(input())

for t in range(numTestCases):
    data = input().split()[1:]
    data = list(map(int, data))
    data_len = len(data)
    swap_cnt = 0
    comp_cnt = 0
    gap = data_len//2
        
    while(gap > 0) :
        for i in range(gap, data_len):
            gap_cnt = 0
            for j in range(i - gap, -1, -gap):
                comp_cnt += 1
                if (data[i-(gap_cnt*gap)] < data[j]):
                    data[i-(gap_cnt*gap)], data[j] = data[j], data[i-(gap_cnt*gap)]
                    swap_cnt += 1
                    gap_cnt += 1
                else : 
                    break
        gap = gap//2
                
    print(comp_cnt, swap_cnt)