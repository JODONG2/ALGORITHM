import sys 
"""
5 5
#####
#..B#
#.#.#
#RO.#
#####
"""
ans = 11
def f(B,bx,by,rx,ry,cnt, before_d): 
    global ans 
    if cnt == 11 : 
        return 
    if ans < cnt : return 
    for d in range(4): 
        if before_d % 2 == d % 2 and cnt != 1: 
            continue 
        temp = [b[:] for b in B]
        # temp[bx][by] = "." 
        # temp[rx][ry] = "."
        nbx,nby,nrx,nry = move(temp,bx,by,rx,ry,d)
        # temp[nbx][nby] = "B"
        # temp[nrx][nry] = "R"
        # print(cnt)
        # for b in temp:
        #     print(b)
        # print("__________________")
        if nbx == -1 : 
            ans = min(ans,cnt)
            # print("HIT : ", cnt,bx,by,rx,ry)
            return 
        if not visited[nbx][nby][nrx][nry] < cnt :
            visited[nbx][nby][nrx][nry] = cnt
            f(temp,nbx,nby,nrx,nry,cnt+1, d) 
            
    

def move(board,bx,by,rx,ry,d): 
    nbx = bx 
    nby = by 
    nrx = rx 
    nry = ry 
    rcnt = 0 
    bcnt = 0 
    while (0<=nbx<N and 0<=nby<M and board[nbx][nby]!='#') :
        nbx += dx[d] 
        nby += dy[d] 
        bcnt += 1 
        if 0<=nbx<N and 0<=nby<M and board[nbx][nby] == 'O' : 
            return bx,by,rx,ry 
    if nbx != bx or nby != by : 
        nbx -= dx[d] 
        nby -= dy[d] 
    while (0<=nrx<N and 0<=nby<M and board[nrx][nry] != '#'): 
        nrx += dx[d] 
        nry += dy[d] 
        rcnt += 1 
        if 0<=nrx<N and 0<=nry<M and board[nrx][nry] == 'O': 
            return -1,-1,-1,-1
    if nrx != rx or nry != ry : 
        nrx -= dx[d] 
        nry -= dy[d] 

    if nbx == nrx and nby == nry : 
        if rcnt>bcnt : 
            nrx -= dx[d] 
            nry -= dy[d] 
        else : 
            nbx -= dx[d] 
            nby -= dy[d] 

    return nbx,nby,nrx,nry 



N,M  = map(int,sys.stdin.readline().split()) 
board = [list(sys.stdin.readline()[:-1]) for _ in range(N)] 
bx,by,rx,ry = 0,0,0,0
for i in range(N):
    for j in range(M): 
        if board[i][j] == "B": 
            bx = i 
            by = j 
        elif board[i][j] == "R": 
            rx = i 
            ry = j 

visited = [[[[11 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[bx][by][rx][ry] = 0 
# bx by rx ry 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
f(board,bx,by,rx,ry,1, 0)
if ans == 11 : 
    ans = -1
print(ans)
