from copy import deepcopy

#바이러스 2
#벽 1
#나띵 0

dx = [0,0,1,-1]
dy = [-1,1,0,0]
N,M = map(int,input().split()) 
lab = []
for _ in range(N):
    lab.append(list(map(int,input().split())))
max_clean = 0

def wall (start, cnt):
    global max_clean 
    if cnt == 3 : 
        copy_lab = deepcopy(lab)
        for i in range(N):
            for j in range(M):
                spread_virus(copy_lab,j,i)
        clean =0 
        for k in range(N):
            clean+= copy_lab[k].count(0)
        max_clean = max(clean, max_clean)
    else:
        for i in range(start, N*M):
            r = i // M 
            c = i % M
            if lab[r][c] == 0 :
                lab[r][c] = 1 
                wall(i,cnt+1)
                lab[r][c] =0 

def spread_virus(arr,x,y):
    if arr[y][x] == 2:
        for i in range(4):
            new_x = x+dx[i] 
            new_y = y+dy[i] 
            if 0<= new_x < M and 0<=new_y<N and arr[new_y][new_x] == 0: 
                arr[new_y][new_x] = 2 
                spread_virus(arr,new_x,new_y)

wall(0,0)
print(max_clean)



