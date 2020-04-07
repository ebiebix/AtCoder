
row,col = map(int,input().split())
senbei = []
result = 0
import copy
#import numpy as np
for i in range(row):
    r_senbei = list(map(int,input().split()))
    senbei.append(r_senbei)
#senbei = np.array(senbei)
for i in range(2**row):
    #tmp_senbei = copy.deepcopy(senbei)
    c_list = [0]*col
    for j in range(row):
        if((i>>j)&1):
            for c in range(col):
                if(senbei[j][c] == 0):
                    c_list[c] += 1
        else:
            for c in range(col):
                if(senbei[j][c] == 1):
                    c_list[c] += 1
    total = 0
    for c in c_list:
        total += max(c,row - c)
        # if c < row/2:
        #     r_total = row - c
        # else:
        #     r_total = c
    result = max(total,result)
print(result)
