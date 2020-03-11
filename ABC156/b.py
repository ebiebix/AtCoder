n,k = map(int,input().split())
def base10toN(X,N):
    if(int(X/N)):
        return base10toN(int(X/N),N)+str(X%N)
    return str(X%N)
print(len(str(base10toN(n,k))))