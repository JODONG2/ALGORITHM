import sys 
cnt = int(sys.stdin.readline())
con_cnt = int(sys.stdin.readline()) 

graph = [i for i in range(cnt+1)]

def find(a):
    if a == graph[a] : 
        return a 
    else : 
        graph[a] = find(graph[a])
        return graph[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b :
        graph[b] = a
    elif a>b :
        graph[a] = b  

for _ in range(con_cnt):
    a,b = map(int,sys.stdin.readline().split())
    union(a,b)
answer = 0 
for g in graph:
    if find(g) == 1 : 
        answer+=1
print(answer-1)

"""
10
7
1 2
2 3
3 4 
5 6
7 8
8 9
9 1
"""