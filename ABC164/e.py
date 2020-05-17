s = int(input())
G =[2019]
g = 2019
while g <= s:
    g += 2019
    G.append(g)
con = 0
print(len(G))
for i in G:
    #print(i)
    con += str(s).count(str(i))
print(con)
