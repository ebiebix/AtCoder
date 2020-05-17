a,b,h,m = map(int,input().split())

import math
deg_a = (360.0/12.0)*h+(360.0/12.0)*(m/60)
deg_b = (360.0/60.0)*m
deg = abs(deg_a-deg_b)
#print(deg_a,deg_b,deg)
d = math.sqrt((math.sin(math.radians(deg))*a)**2+(b-a*math.cos(math.radians(deg)))**2)
print('{:.11g}'.format(d))