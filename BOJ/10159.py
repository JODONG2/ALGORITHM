
import sys 
from collections import deque 
def cnt_unknown(number,n):
    q = deque([number])
    visit = [True for _ in range(n+1)]
    visit[number]= False 
    ret = 0 
    while q : 
        num = q.popleft() 
        for n in graph_big[num] : 
            if visit[n] : 
                visit[n] = False 
                q.append(n) 
                ret+=1 
    q = deque([number]) 
    while q : 
        num = q.popleft()
        for n in graph_small[num] : 
            if visit[n] : 
                visit[n] = False 
                q.append(n)
                ret += 1 
    
    return ret 
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph_big = [[]for _ in range(n+1)] 
graph_small = [[] for _ in range(n+1)] 
for _ in range(m): 
    x,y = map(int,sys.stdin.readline().split())
    graph_big[x].append(y)
    graph_small[y].append(x)

for i in range(1,n+1):
    print(n - cnt_unknown(i,n) - 1)

