n = int(input())
A = list(map(int,input().split()))
B = []
for i in A:
    if (int(i)%2 == 0):
        B.append(int(i))

for j in B:
    if (int(j)%3 == 0 or int(j)%5 == 0):
        pass
    else:
        print('DENIED')
        exit()
print('APPROVED')