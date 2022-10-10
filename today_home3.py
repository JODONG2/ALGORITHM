from collections import deque 
from copy import deepcopy
answer = 0
def is_possible(n,m,home,num):
    global answer 
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    q = deque()
    succ = set()
    for i in range(n):
        for j in range(m):
            if home[i][j] == 0 :
                q.append([i,j])
                break
        if q:
            break
    while q : 
        x,y = q.popleft()
        home[x][y] = -1
        for px,py in zip(dx,dy):
            nx,ny = x+px, y+py 
            if 0<=nx<n and 0<=ny<m:
                if home[nx][ny] == 0:
                    home[nx][ny] = -1
                    q.append([nx,ny])
                elif home[nx][ny] != 0:
                    succ.add(home[nx][ny])

    for h in home:
        if 0 in h :
            return 0

    suc = False
    if -1 in home[0]:
        suc = True  
    elif -1 in home[-1]:
        suc= True
    else:
        for h in home:
            if h[0]==-1 or h[-1]==-1:
                suc = True
                break
    if not suc :
        return 0

    if len(succ) == num :
        # for ho in home:
        #     print(ho)
        # print("-"*10)
        answer+=1
        # print(succ,num,answer)
        # print("-"*10)
        return 1
    else :
        return 0

def dfs(n,m,room,bath,home2,num,already_room2,already_bath2):
    answer =0 
    home = deepcopy(home2)
    already_room = deepcopy(already_room2)
    already_bath = deepcopy(already_bath2)
    if room ==0 and bath ==0:
        return is_possible(n,m,home,num)
    for i in range(n):
        for j in range(m):
            if already_room[i][j] and already_bath[i][j]:
                continue
            check_room = True 
            check_bath = True
            if j == m-1 : 
                check_room = False
                if i+1<n and home[i+1][j]!=0 and home[i][j]!=0:
                    check_bath = False 
            elif i == n-1 :
                check_room = False
                if j+1<n and home[i][j+1]!=0 and home[i][j]!=0:
                    check_bath = False
            else:
                for q in range(2):
                    for w in range(2):
                        if i+q<n and j+w <m and home[i+q][j+w]:
                            check_room = False
                            check_bath = False
                            if q==1 and w ==1 :
                                check_bath = True
                            break #방 들어갈 자리 있음
                    if not check_room:
                        break

            if not already_room[i][j] and check_room and room>0 :
                already_room[i][j] = True
                for q in range(2):
                    for w in range(2):
                        home[i+q][j+w] = num

                answer += dfs(n,m,room-1,bath,home,num+1,already_room,already_bath) #방 넣음
                # already_room[i][j] = False 
                for q in range(2):
                    for w in range(2):
                        home[i+q][j+w] = 0

            if not already_bath[i][j] and check_bath and bath>0:
                already_bath[i][j] = True 
                if i + 1 < n and home[i+1][j] == 0 and home[i][j]==0:
                    for q in range(2):
                        home[i+q][j] = num 
                    answer+=dfs(n,m,room,bath-1,home,num+1,already_room,already_bath)
                    home[i+1][j] = 0
                    home[i][j] = 0
                if j + 1 < m and home[i][j+1]==0 and home[i][j] == 0:
                    for q in range(2):
                        home[i][j+q] = num
                    answer+=dfs(n,m,room,bath-1,home,num+1,already_room,already_bath)
                    # already_bath[i][j] = False
                    home[i][j+1],home[i][j] =0,0
    return answer       

def solution(n, m, room, bath):
    # 1<=n,m<=5
    #room 방의 개수 -> 2x2
    #bath 화장실 개수 -> 1x2 2x1
    #고립되면 안됨
    #버려지는 공간 있으면 안됨 // 집이 방이나 화장실로 나뉘어지면 안됨 
    #입구를 설치하기 위해 빈공간중 최소 한 공간은 집의 테두리와 인접해있어야함 
    answer = -1
    global answer_home
    home = [[0 for _ in range(m)] for _ in range(n)]
    already_room = [[False for _ in range(m)] for _ in range(n)]
    already_bath = [[False for _ in range(m)] for _ in range(n)]
    answer = dfs(n,m,room,bath,home,1,already_room,already_bath)
    return answer