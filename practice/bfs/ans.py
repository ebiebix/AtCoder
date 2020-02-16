from queue import Queue
R, C = map(int, input().split(' '))
Sy, Sx = map(int, input().split(' '))
Gy, Gx = map(int, input().split(' '))
L = [[s for s in input()] for _ in range(R)]
print(L)
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
q = Queue()
ans = 0

q.put([(Sy, Sx)])
L[Sy-1][Sx-1] = '#'
print(q.get())
while not q.empty():
    pos = q.get()
    valid_pos = []
    print(pos)
    for p in pos:
        for m in move:
            y, x = p[0]+m[0], p[1]+m[1]
            if y == Gy and x == Gx:
                ans += 1
                print(ans)
                exit()
            if L[y-1][x-1] == '.':
                L[y-1][x-1] = '#'
                valid_pos.append((y, x))
    if len(valid_pos) != 0:
        print(valid_pos)
        q.put(valid_pos)
    ans += 1
print(ans-1)