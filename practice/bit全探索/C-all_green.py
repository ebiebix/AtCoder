n,g = map(int,input().split())
P = []
C = []
for i in range(n):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c)
count_ans = 10001
for i in range(2**(len(C))):
    bag = []
    total = 0
    total_ans = 0
    count = 0
    for j in range(len(C)):
        if ((i>>j)&1):
            total += (int(j)+1)*100*P[j]+C[j]
            count += P[j]
            if (count<count_ans and total>g):
                count_ans = count
        else:
            if (total < g):
                print('aaa')
                for m in range(1,int(P[j])):
                    if((int(j)+1)*100*int(m)+total > g and count+int(m)<count_ans):
                        print('bbb')
                        total += (int(j)+1)*100*int(m)+total
                        count_ans = count + int(m)
    print(total)
    print(count_ans)
