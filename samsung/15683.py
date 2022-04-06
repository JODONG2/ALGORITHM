"""
1 : 한방향
2 : 상하, 좌우 
3 : 90도 
4 : 하나 뺴고 다 
5 : 4방향 
6 : 벽 

6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5

4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0

사각지대의 수 == 0의 수 
회전 90도씩 가능 
"""

#TODO: 데이터입력 -> 카메라 위치 찾기
n,m = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]
cam = [] 
for i in range(n):
    for j in range(m): 
        if room[i][j] != 0 and room[i][j] !=6: 
            cam.append([i,j,room[i][j]])

#TODO: 카메라 종류 별 보는곳세기 -> 한방향씩 채우기 
def show_r(x,y):
    while y < m and room[x][y] != 6:
        room[x][y] = 7
        y+=1 
def show_l(x,y): 
    while y>=0 and room[x][y] != 6: 
        room[x][y] = 7 
        y-=1 
def show_u(x,y):
    while x>=0 and room[x][y] != 6:
        room[x][y] = 7 
        x-=1 
def show_d(x,y):
    while x<n and room[x][y] != 6:
        room[x][y] = 7 
        x+=1 

def copy_room(arr): 
    ret = [[0 for _ in range(m)] for _ in range(n)] 
    for i in range(n): 
        for j in range(m): 
            ret[i][j] = arr[i][j]
    return ret 

def count(cnt):
    ret = 0 
    for i in range(n):
        for j in range(m): 
            if room[i][j] == 0 : 
                ret += 1 
                if ret>=cnt : 
                    return ret
    # for r in room :
    #     print(r)
    # print("*"*50)
    return ret 
#TODO: 사각지대 수 세기 

def dfs(cam_index,cnt):
    global room
    global cam 
    if len(cam) <= cam_index : 
        compare = count(cnt)
        if cnt > compare : 
            cnt = compare 
        return cnt 
    x,y,case = cam[cam_index][0], cam[cam_index][1], cam[cam_index][2] 
    if case == 1 :
        temp = copy_room(room) 
        show_r(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_l(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_u(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_d(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)

    elif case ==2 : 
        temp = copy_room(room) 
        show_r(x,y)
        show_l(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_u(x,y)
        show_d(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
    elif case == 3 : 
        temp = copy_room(room) 
        show_r(x,y)
        show_u(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_r(x,y)
        show_d(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_l(x,y)
        show_d(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
        temp = copy_room(room) 
        show_l(x,y)
        show_u(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)
    elif case == 4 : 
        temp = copy_room(room) 
        show_r(x,y)
        show_d(x,y)
        show_l(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)

        temp = copy_room(room) 
        show_r(x,y)
        show_d(x,y)
        show_u(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)

        temp = copy_room(room) 
        show_r(x,y)
        show_u(x,y)
        show_l(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)

        temp = copy_room(room) 
        show_u(x,y)
        show_d(x,y)
        show_l(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)

    elif case == 5 : 
        temp = copy_room(room) 
        show_r(x,y)
        show_d(x,y)
        show_l(x,y)
        show_u(x,y)
        cnt = dfs(cam_index+1,cnt)
        room = copy_room(temp)

    return cnt 
if __name__ == "__main__":

    print(dfs(0,float("inf")))