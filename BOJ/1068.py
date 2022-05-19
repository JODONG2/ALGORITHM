import sys 

def dfs(del_num, graph,cnt):
    graph[del_num] = -2 
    for i in range(cnt):
        if graph[i] == del_num : 
            dfs(i,graph,cnt)

cnt = int(input())
graph = list(map(int,sys.stdin.readline().split()))
delete = int(sys.stdin.readline()) 
dfs(delete, graph,cnt )

answer = 0 
for i in range(cnt):
    if graph[i] != -2 and not i in graph : 
        answer+=1 
print(answer)
