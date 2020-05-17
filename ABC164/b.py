import math
a,b,c,d = map(int,input().split())
ao_hp = math.ceil(c/b)
taka_hp = math.ceil(a/d)
#(taka_hp,ao_hp)
if(taka_hp > ao_hp):
    print('Yes')
elif(taka_hp < ao_hp):
    print('No')
else:
    print('Yes')