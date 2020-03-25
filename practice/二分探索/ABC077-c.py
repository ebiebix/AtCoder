n = int(input())
A = list(map(int,input().split()))
A.sort()
B = list(map(int,input().split()))
C = list(map(int,input().split()))
C.sort()

total = 0
tmp_a_t = 0
tmp_c_t = 0
from bisect import bisect_left,bisect_right
for i,b in enumerate(B):
    tmp_a = bisect_left(A,b)
    tmp_c = len(C)-bisect_right(C,b)
    #print(tmp_a,tmp_c)
    total += tmp_a*tmp_c
# print(tmp_a,tmp_c_t)
# total += tmp_a*tmp_c_t
print(total)

