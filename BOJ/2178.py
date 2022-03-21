from collections import deque

def search(N,M,maps): 
    q = deque()
    q.append((0,0)) 
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while q: 
        x,y = q.popleft() 
        for px,py in zip(dx,dy): 
            if 0<=x+px<N and 0<=y+py<M and maps[x+px][y+py] == 1 :
                maps[x+px][y+py] = maps[x][y] + 1 
                q.append((x+px,y+py))
    return maps[-1][-1]
if __name__ == "__main__":
    N,M = map(int,input().split()) 
    maps = [list(map(int,input())) for _ in range(N)]
    print(search(N,M,maps))
    # for map in maps:
    #     print(map)
