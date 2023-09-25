numTestCases = int(input())

for t in range(numTestCases):
    data = input().split()[1:]
    data = list(map(int, data))
    data_len = len(data)
    swap_cnt = 0
    comp_cnt = 0
    shrink = 1.3
    gap = data_len
    sorting = False
    
    while(gap != 1 or (not sorting)):
        gap = int(gap/shrink)
        sorting = True
        if gap < 1 :
            gap = 1
        
        for i in range(data_len - gap):
            comp_cnt += 1
            if (data[i] > data[i+gap]):
                data[i], data[i+gap] = data[i+gap], data[i]
                swap_cnt += 1
                sorting = False
                
    print(comp_cnt, swap_cnt)