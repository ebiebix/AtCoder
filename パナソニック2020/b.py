h,w = map(int,input().split())
if(h*w%2 ==0):
    print(int(h*w/2))
else:
    print(int(h*w/2)+1)