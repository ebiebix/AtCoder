n,k = map(int,input().split())
P = list(map(int,input().split()))
sum_a = 0
index = 0

for i in range(k):
    sum_a += P[i]
num = sum_a
for j in range(1,n-k+1):
    num += P[j+k-1]
    #print(num)
    num -= P[j-1]
    #print(num)
    if(sum_a<num):
        index = j
        sum_a = num

total = 0.0
for m in range(index,index+k):
    total += sum(list(range(P[m]+1)))/P[m]
print(total)