s = list(input())
q = int(input())
con = 0
for i in range(q):
    tmp_q = list(input().split())
    if(int(tmp_q[0])==1):
        #s.reverse()
        con += 1
        #print(s)
    else:
        list_tmp = []
        #print(tmp_q)
        if(int(tmp_q[1])==1 and con%2==0):
            list_tmp = list(tmp_q[2])
            #print(list_tmp)
            list_tmp.extend(s)
            s = list_tmp
            #print(s)
        elif(int(tmp_q[1])==1 and con%2==1):
            s.extend(list(tmp_q[2]))
        elif(int(tmp_q[1])==2 and con%2==1):
            list_tmp = list(tmp_q[2])
            #print(list_tmp)
            list_tmp.extend(s)
            s = list_tmp
            #print(s)
        else:
            #print(tmp_q)
            s.extend(list(tmp_q[2]))
if (con%2==1):
    s.reverse()
print(''.join(s))