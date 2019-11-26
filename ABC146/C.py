tmp = input().split(" ")
A = int(tmp[0])
B = int(tmp[1])
X = int(tmp[2])
l = 0
r = 10**9+1

def func(mid):
    return int(A*mid+B*len(str(mid)))
    #print((A*mid)+(B*int(len(str(mid)))))


while(r-l>1):
    #二分探索をする
    mid = int((r+l)/2)
    #print(mid)
    if(func(mid) <= X):
        l = mid
    else:
        r = mid

print(l)
