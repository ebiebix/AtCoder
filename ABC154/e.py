n = int(input())
k = int(input())
count = 0
for i in range(n+1):
    if(str(i).count('0')==len(str(i))-k):
        count +=1
print(count)