s = list(input())
con = 0
if (len(s)%2 == 0):
    for i in range(0,len(s),2):
        if (s[int(i)] == 'h'):
            if(s[int(i)+1] =='i'):
                con += 2
            else:
                print('No')
                exit()
        else:
            print('No')
            exit()
    if (con == len(s)):
        print('Yes')
        exit()
print('No')
exit()