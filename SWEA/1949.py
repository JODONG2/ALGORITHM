 #N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.
 #각 숫자는 지형의 높이를 나타낸다.

"""
등산로는 가장 높은 봉우리에서 시작해야 한다.

② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
       즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
 """
#긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.
#2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
#3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
#4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
#5. 지도에서 가장 높은 봉우리는 최대 5개이다.
#7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.
from collections import deque 
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def search_path(world,start,n,k):
    answer = 1 
    for x,y in start: 
        q = deque([(x,y,True,[(x,y)],1, world[x][y])])
        while q: 
            x,y,check,visit,dist,h = q.popleft()
            print(visit)
            if answer < dist : 
                answer = dist 
            for px,py in zip(dx,dy):
                nx,ny = x+px,y+py 
                if 0<=nx<n and 0<=ny<n and not ((nx,ny) in visit):
                    temp = visit[:]
                    if world[nx][ny] < h :
                        temp.append((nx,ny))
                        q.append((nx,ny,check,temp,dist+1, world[nx][ny]))
                    elif world[nx][ny] - k < h and check : 
                        temp.append((nx,ny)) 
                        q.append((nx,ny,not check,temp, dist+1, h-1))
    return answer 

tc = int(input()) 
for t in range(1,tc+1):
    n,k = map(int,input().split()) 
    world = [list(map(int,input().split())) for _ in range(n)]
    start= [(0,0)] 
    maxi = 0 
    for i in range(n):
        for j in range(n):
            if maxi < world[i][j] :
                start = [(i,j)] 
                maxi = world[i][j]
            elif maxi == world[i][j] :
                start.append((i,j))            
    print(search_path(world,start,n,k))
            

 
"""
1     
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
"""