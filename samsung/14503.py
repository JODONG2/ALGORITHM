from collections import deque 

def input_data():
    N,M = map(int,input().split())
    r,c,d = map(int,input().split()) 
    room = [list(map(int,input().split())) for _ in range(N)]
    return N,M,r,c,d,room 

def robot_move(r,c,d): 
    pass 

def robot(N,M,r,c,d,room): 
    answer = 1
    room[r][c] = 2
    # 0북 1동 2남 3서 
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque() 
    q.append((r,c,d))
    while q : 
        r,c,d = q.popleft()
        check = False 
        for _ in range(4):
            d = d-1 if d-1 >= 0 else 3 
            px, py = dx[d], dy[d] 
            if 0<=r+px<N and 0<=c+py<M and room[r+px][c+py] == 0 :
                q.append((r+px,c+py,d))
                room[r+px][c+py] = 2
                check = True 
                answer+=1
                break 
        if not check :

            if 0<=r-dx[d]<N and 0<=c-dy[d]<M and room[r-dx[d]][c-dy[d]] != 1:
                q.append([r-dx[d],c-dy[d],d])
                check= True 
            if not check: 
                return answer
    return answer 

if __name__ == "__main__":
    N,M,r,c,d,room = input_data() 
    print(robot(N,M,r,c,d,room))
    
    

