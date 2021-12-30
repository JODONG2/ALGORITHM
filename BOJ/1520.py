#내리막길
from collections import deque
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def dfs(x,y) -> int:
    if x==W-1 and y == H-1:
        return 1
    if dp[y][x] != -1 :
        return dp[y][x]
    dp[y][x] = 0 
    for d in range(4):
        new_x = x+dx[d]
        new_y = y+dy[d]
        if 0<= new_x < W and 0<= new_y < H and  world[new_y][new_x] < world[y][x]:
            dp[y][x] += dfs(new_x,new_y)
    return dp[y][x]

H,W = map(int,input().split())
world = []
for _ in range(H):
    world.append(list(map(int,input().split())))
dp = [[-1 for _ in range(W)] for _ in range(H)]
dp[H-1][W-1] = 1
print(dfs(0,0))
