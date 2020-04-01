#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

for m in M:
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if((i>>j)&1):
                tmp += A[j]
        if(tmp == m):
            print('yes')
            break
    if(tmp == m):
        pass
    else:
        print('no')