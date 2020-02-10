n,k = map(int,input().split())
P = list(map(int,input().split()))
sum_a = 0
index = 0
for i in range(n):
    num = 0
    
    if (int(i)+k<=n):
        for j in range(int(i),int(i)+k):
            num += P[j]
        if(sum_a<num):
            index = i
            sum_a = num
            #print(sum_a,index)
total = 0.0
for m in range(index,index+k):
    total += sum(list(range(P[m]+1)))/P[m]
print(total)