"""
5
0 1 1 0 0
1 0 0 1 1
1 0 0 1 1
0 1 1 0 0
0 1 1 0 0
"""
import sys 
n = int(sys.stdin.readline())
connection = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def find(x):
    if graph[x] == x :
        return x 
    else: 
        graph[x] = x 
        return find(graph[x])

def union(x,y):
    x = find(x)
    y = find(y) 
    if graph[x] == graph[y] : 
        return 
    if graph[x]>graph[y]:
        graph[x] = graph[y] 
    else : 
        graph[y] = graph[x] 

graph = [ i for i in range(n) ]
for i in range(n):
    for j in range(n):
        if graph[j] != j : 
            continue
        if i!=j and connection[i][j] == 0 :
            union(i,j)
            print(i,j,graph)
len_group = len(set(graph))
answer = [[] for _ in range(n)]
for g in range(n):
    answer[graph[g]].append(g+1)
answer2 = []
check = False 
for a in answer : 
    if not a :
        continue 
    if len(a)<=1 : 
        check = True 
        break 
    else: 
        answer2.append(a)
if check: 
    print(0)
else : 
    print(len(answer2))
    for a in answer2 :
        print(*a)



