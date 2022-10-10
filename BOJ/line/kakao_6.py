import heapq
dx = [1,0,0,-1]
dy = [0,-1,1,0]
def solution(n, m, x, y, r, c, k):
    x-=1
    y-=1
    r-=1
    c-=1
    board = [[['' for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    cmd = ['d','l','r','u']
    q = []
    heapq.heappush(q,('',x,y,0)) 
    dif_xr = abs(x - r)
    dif_yc = abs(y - c) 
    xr_yc = dif_xr + dif_yc 
    if xr_yc % 2 != k % 2: return 'impossible'
    while q : 
        s,x,y,cnt = heapq.heappop(q)
        # print(s)
        if cnt == k : 
            if(x==r and y==c): 
                return s
            continue
        if cnt > k : 
            continue
        for d in range(4) : 
            nx,ny = dx[d] + x , dy[d] + y 
            if (0<=nx<n and 0<=ny<m and (board[nx][ny][cnt] == '' or board[nx][ny][cnt] > s)):
                board[nx][ny][cnt] = s 
                heapq.heappush(q,(s+cmd[d],nx,ny,cnt+1))
        
    return 'impossible'

print(solution(3,4,2,3,3,1,5))