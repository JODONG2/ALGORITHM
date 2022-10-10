import sys 
n,m = map(int,sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
accum_sum = [[0 for _ in range(n)] for _ in range(n)]
num = 0 
for i in range(n):
    for j in range(n): 
        if i==0 and j == 0 : 
            accum_sum[i][j] = maps[i][j] 
        elif i == 0 : 
            accum_sum[i][j] = maps[i][j] + accum_sum[i][j-1]
        elif j == 0 : 
            accum_sum[i][j] = maps[i][j] + accum_sum[i-1][j]
        else: 
            accum_sum[i][j]= accum_sum[i-1][j] + accum_sum[i][j-1] - accum_sum[i-1][j-1] + maps[i][j]
        
for _ in range(m):
    x,y,xx,yy = map(int,sys.stdin.readline().split())
    x-=1
    y-=1
    xx-=1
    yy-=1 
    if x == 0 and y == 0:
        print(accum_sum[xx][yy])
    elif x == 0 : 
        print(accum_sum[xx][yy] - accum_sum[x][y-1])
    elif y == 0 : 
        print(accum_sum[xx][yy] - accum_sum[x-1][y])
    else:
        print(accum_sum[xx][yy] + accum_sum[x-1][y-1] - accum_sum[x-1][yy] - accum_sum[xx][y-1])
