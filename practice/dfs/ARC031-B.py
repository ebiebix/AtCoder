##読み込み
graph = []
count = 0
for i in range(10):
    s = input()
    if "o" in s:
        start_point = [i,s.index("o")]
    count += s.count('o')
    graph.append(s)

##DFSで一つの島になっているか確認(探索できたマス=埋立地+陸地の数)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def DFS(graph):
    not_visited = []
    not_visited=[[True for i in range(10)] for j in range(10)]
    stack = [start_point]
    not_visited[start_point[0]][start_point[1]] = False
    count_graph = 0
    while len(stack):
        now_point = stack.pop()
        for i in range(4):
            if count_graph == count:
                return True
            
            else:
                #print(now_point[0],dx[i],now_point,dy[i])
                serch_point = [now_point[0]+dx[i],now_point[1]+dy[i]]
                if 0 <= serch_point[0] < 10 and 0 <= serch_point[1] < 10:
                    if graph[serch_point[0]][serch_point[1]] != 'x' and not_visited[serch_point[0]][serch_point[1]]:
                        stack.append([serch_point[0],serch_point[1]])
                        not_visited[serch_point[0]][serch_point[1]] = False
                        count_graph += 1
    return False

##どこを埋めるか全探索
for i in range(10):
    for j in range(10):
        graph_tmp = graph.copy()
        #print(graph,len(graph))
        if(graph_tmp[int(i)][int(j)] == 'x'):
            tmp = graph_tmp[int(i)][:int(j)]+'o'+graph_tmp[int(i)][int(j)+1:]
            graph_tmp[i] = tmp
            #print(graph_tmp,graph)
            if DFS(graph_tmp):
                print('YES')
                exit()
print('NO')


