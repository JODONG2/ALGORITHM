
from collections import deque 
def search_max(ox,oy,n,m,city,limit):
    ret = 0
    ret2 = 0
    q = deque([(ox,oy,1)])
    check = [[True for _ in range(n)] for _ in range(n)]
    check[ox][oy] = False
    cost = 5 
    if city[ox][oy] == 1 : 
        ret2 = 1 
        cost -= m 
        ret = 1 
    before_dist = 1 

    while q :
        x,y,dist= q.popleft() 
        if dist != before_dist : 
            # print(q,ret,ret2, cost)
            if cost <= 0 and ret<ret2: 
                ret = ret2
            c = (dist+1)*(dist+1) + (dist)*(dist)
            if c > limit or ret2 >= limit//m :
                break 
            before_dist = dist 
            cost = c - ret2 * m

        for px,py in zip(dx,dy): 
            nx,ny = x+px,y+py 
            if 0<=nx<n and 0<=ny<n and check[nx][ny] : 
                check[nx][ny] = False
                if city[nx][ny] == 1 : 
                    cost -= m 
                    ret2+=1 
                q.append((nx,ny,dist+1))
    return ret 
    

def start():
    n,m = map(int,input().split()) 
    city = [list(map(int,input().split() ) ) for _ in range(n)]
    house = 0 
    for i in range(n):
        for j in range(n): 
            if city[i][j] == 1 : 
                house+=1
    answer = 0 
    limit = house*m
    # search_max(3,3,n,m,city,limit)
    for x in range(n):
        for y in range(n):
            answer = max(answer, search_max(x,y,n,m,city,limit))
    return answer

test_case = int(input()) 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for t in range(1,test_case+1):
    print(f"#{t} {start()}")

"""
1
8 3
0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0
1 0 0 0 0 0 0 0

"""