
dx = [0,0, 1,1,1, -1,-1,-1]
dy = [1,-1, 0,1,-1, 0,1,-1]

def dfs(arr,i,j,max_h,max_w):
    arr[i][j] = 0
    for d in range(8):
        dir_y = i+dy[d] 
        dir_x = j+dx[d]
        if dir_y < 0 or dir_y >=max_h or dir_x <0 or dir_x >= max_w: 
            continue 
        if arr[dir_y][dir_x] == 1 : 
            dfs(arr,dir_y,dir_x,max_h,max_w)

while(True):
    W,H = map(int, input().split()) 
    if W==0 and H ==0 :
        break
    island = []
    answer = 0
    for _ in range(H):
        island.append(list(map(int,input().split())))
    
    for h in range(H):
        for w in range(W): 
            if island[h][w] == 1: 
                dfs(island,h,w,H,W)
                island[h][w] = 1 
                answer +=1 
    print (answer)
    
"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""
        
