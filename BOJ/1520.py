#내리막길
from collections import deque

def dfs(world:list,
        answer:int,
        H:int,
        W:int) -> int:
    #내리막길로만 가는 방법의 수를 return 
    position = deque([[0,0]])
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    dp = [[-1 for _ in range(W)] for _ in range(H)]
    dp[H-1][W-1] = 1
    while position :
        x,y = position.pop()
        for d in range(4):
            new_x = x+dx[d]
            new_y = y+dy[d]
            if 0<= new_x < W and 0<= new_y < H and  world[new_y][new_x] < world[y][x]: 
                if new_x == W-1 and new_y == H-1:
                    answer+=1 
                    continue
                position.append([new_x, new_y])
    return answer

if __name__ == '__main__':
    H,W = map(int,input().split())
    world = []
    for _ in range(H):
        world.append(list(map(int,input().split())))
    answer = 0 
    answer = dfs(world,answer,H,W)
    print(answer)
