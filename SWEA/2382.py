

direction = [0,(-1,0),(1,0),(0,-1),(0,1)]
change_direction = {1:2, 2:1, 3:4, 4:3}
def move(clust,N,M,cell2):
    temp_space = [[0 for _ in range(N)] for _ in range(N)]
    cell = [cell2,temp_space]
    for index in range(M):
        clust_key = list(clust.keys())
        for key in clust_key : 
            i,j,cnt,d,temp_cnt = clust[key] 
            x=i
            y=j
        # for i in range(N):
        #     for j in range(N):
        #         if cell[index%2][i][j] != 0 :  #clust = x,y,cnt,d
        #             x,y,cnt,d,temp_cnt = clust[cell[index%2][i][j]]
            nx,ny = x+direction[d][0] , y+ direction[d][1] 
            if 0<nx<N-1 and 0<ny<N-1 : 
                if cell[(index+1)%2][nx][ny] != 0 :
                    _,_,cnt2,d2,temp_cnt2 = clust[cell[(index+1)%2][nx][ny]]
                    if temp_cnt2 < temp_cnt : 
                        d2 = d
                        temp_cnt2 = temp_cnt
                    cnt2+=cnt
                    del clust[cell[index%2][i][j]]
                    clust[cell[(index+1)%2][nx][ny]][3] = d2 
                    clust[cell[(index+1)%2][nx][ny]][2] = cnt2
                    clust[cell[(index+1)%2][nx][ny]][4] = temp_cnt2
                    cell[index%2][i][j] = 0 
                else:
                    clust[cell[index%2][i][j]] = [nx,ny,cnt,d,temp_cnt]
                    cell[(index+1)%2][nx][ny] = cell[index%2][i][j]
                    cell[index%2][i][j] = 0 
            else : 
                d = change_direction[d]
                cnt = cnt//2
                if cnt == 0 : 
                    del clust[cell[index%2][i][j]]
                    cell[index%2][i][j] = 0 
                else:
                    cell[(index+1)%2][nx][ny] = cell[index%2][i][j]
                    clust[cell[index%2][i][j]] = [nx,ny,cnt,d,temp_cnt//2]
                    cell[index%2][i][j] = 0 
        clust_key = list(clust.keys())
        for key in clust_key:
            clust[key][4] = clust[key][2]               
    if M%2 == 1 : 
        return temp_space
    else :
        return cell2 


test_case = int(input()) 
for t in range(1,test_case+1):
    answer = 0 
    N,M,K = map(int,input().split()) 
    cell = [[0 for _ in range(N)] for _ in range(N)]
    clust = {} 
    for c_num in range(1,K+1):
        x,y,cnt,dir = map(int,input().split()) 
        clust[c_num] = [x,y,cnt,dir,cnt]
        cell[x][y] = c_num

    cell = move(clust,N,M,cell)

    for _,value in clust.items():
        answer += value[2]

    print(f"#{t} {answer}")

    """
1
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
    """