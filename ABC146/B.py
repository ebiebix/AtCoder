n = int(input())
string = list(input())
#print(ord("Z"))
for e,i in enumerate(string):
    val = ord(str(i)) + n
    if (val > 90):
        val = 64 + (val - 90)
    string[e] = chr(val)
mojiretu = ''
for x in string:
    mojiretu += x
    
print(mojiretu)
#print(str(string))