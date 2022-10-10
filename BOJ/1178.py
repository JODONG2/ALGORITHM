
v,e = map(int,input().split()) 

graph = [[0 for _ in range(v+1)] for _ in range(v+1)] 

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b : 
        conn[b] = a 
    else:
        conn[a] = b 

def find(a):
    if a == conn[a] :
        return a 
    else:
        conn[a] = find(conn[a])
        return conn[a]

conn = [i for i in range(v+1)]

for _ in range(e):
    start,end = map(int,input().split())
    graph[start][end] = 1 
    graph[end][start] = 1
    union(start,end)
for g in graph:
    print(g) 
print(conn)

"""
11 8
1 2
1 3 
1 4
5 6
5 7 
5 8 
9 10 
9 11 
"""