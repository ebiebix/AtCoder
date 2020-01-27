H = int(input())
num =0
while(h>1):
    h /=2
    num +=1
con = 0
for i in range(num):
    con += 2**int(i)