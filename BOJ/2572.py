"""
5
R G R B G
4 5
1 2 R
1 3 G
2 3 G
1 4 R
4 3 B
"""
import sys 
from collections import deque 
answer =0 

def dfs(card_index,now,point):
    global answer
    if card_index == card_count-1: 
        answer = max(answer,point)
        return 
    for i in range(card_index+1,card_count):
        for next, color in graph[now]:
            if color == cards[i] : 
                dfs(i,next,point+10)
            else:
                dfs(i,next,point)
def bfs(): 
    index = 0
    while index < card_count :  
        for now, point in enumerate(dp[index]) : 
            if index != 0 and (point == 0 or now == 0) :
                continue 
            for next,color in graph[now]: 
                if color == cards[index] : 
                    if dp[index+1][next] > point+10 : 
                        continue 
                    dp[index+1][next] = point + 10
                else :
                    if dp[index+1][next] > point : 
                        continue 
                    dp[index+1][next] = point 
            if index == 0 and now == 1 :
                break 
        index+=1
    return max(dp[index])
card_count = int(sys.stdin.readline())
cards = list(sys.stdin.readline().split())
v,e = map(int,sys.stdin.readline().split()) 
graph = [[] for _ in range(v+1)]
dp = [[0 for _ in range(v+1)] for _ in range(card_count+1)]
# dp[0] = [False for _ in range(v+1)]
for _ in range(e):
    start,end,color = sys.stdin.readline().split() 
    start,end = int(start), int(end)
    graph[start].append((end,color)) 
    graph[end].append((start,color)) 
    
# dfs(-1,1,0)
print(bfs())
# for d in dp:
#     print(d)
