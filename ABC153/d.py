H = int(input())
num =0
while(H>=1):
    H /=2
    num +=1
con = 0
for i in range(num):
    con += 2**int(i)
print(con)