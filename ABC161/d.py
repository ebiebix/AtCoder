k = int(input())

runrun = []

import queue
q = queue.Queue()
for i in range(1,10,1):
    q.put(i)
num = 0
while num <= 3234566667:
    num = q.get()
    runrun.append(num)
    tale = str(num)
    if(tale[-1] == '0'):
        same_tale = tale + '0'
        same_tale = int(same_tale)
        q.put(same_tale)

        max_tale =  tale + '1'
        max_tale = int(max_tale)
        q.put(max_tale)
    elif(tale[-1] == '9'):
        min_tale = tale + '8'
        min_tale = int(min_tale)
        q.put(min_tale)

        same_tale = tale + '9'
        same_tale = int(same_tale)
        q.put(same_tale)
    else:
        v = int(tale[-1])
        min_tale = tale + str(v-1)
        min_tale = int(min_tale)
        q.put(min_tale)

        same_tale = tale + str(v)
        same_tale = int(same_tale)
        q.put(same_tale)

        max_tale =  tale + str(v+1)
        max_tale = int(max_tale)
        q.put(max_tale)

print(runrun[k-1])
