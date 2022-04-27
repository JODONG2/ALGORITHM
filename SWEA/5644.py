

from collections import deque 

dir = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]

def power_range(power,world,power_dic):
    for num, po in enumerate(power) : 
        check = [[True for _ in range(10)] for _ in range(10)]
        x,y,c,p = po 
        q = deque([(y-1,x-1,c)]) 
        
        num += 1 
        power_dic[num] = p 
        check[y-1][x-1] = False 
        if world[y-1][x-1] : 
            if len(world[y-1][x-1]) == 2: 
                if power_dic[world[y-1][x-1][1]] < p : 
                    world[y-1][x-1].pop() 
            
            if power_dic[world[y-1][x-1][0]] > p : 
                world[y-1][x-1].append(num)
            else : 
                world[y-1][x-1].appendleft(num)
        else :
            world[y-1][x-1].append(num)
        while q : 
            y,x,c = q.popleft()
            if c == 0 : 
                break 
            for py,px in dir[1:] : 
                ny,nx = y+py, x+px 
                if 0<=ny<10 and 0<=nx<10 and check[ny][nx] : 
                    if world[ny][nx] : 
                        if len(world[ny][nx])==2: 
                            if power_dic[world[ny][nx][1]] < p : 
                                world[ny][nx].pop()
                            else : 
                                q.append((ny,nx,c-1)) 
                                check[ny][nx] = False 
                                continue 
                        if power_dic[world[ny][nx][0]] > p : 
                            world[ny][nx].append(num)
                        else:
                            world[ny][nx].appendleft(num)
                    else : 
                        world[ny][nx].append(num)
                    q.append((ny,nx,c-1))
                    check[ny][nx] = False 

#dir = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]

def moving(player,world,power_dic):
    x1,y1,r1 = 0,0,0 
    x2,y2,r2 = 9,9,0
    ret = 0 
    if world[x1][y1] : 
        r1 = world[x1][y1][0]
        ret+= power_dic[r1]
    if world[x2][y2] :
        r2 = world[x2][y2][0]
        ret+=power_dic[r2]
    
    for p1,p2 in zip (player[0], player[1]):
        x1,y1 = x1+dir[p1][0], y1+dir[p1][1]
        x2,y2 = x2+dir[p2][0], y2+dir[p2][1] 
        if world[x1][y1] :
            r1 = world[x1][y1][0]
        else : 
            r1 = 0 

        if world[x2][y2] :
            r2 = world[x2][y2][0] 
        else :
            r2 = 0

        div = False 
        if r1 == r2 and r1 != 0 : 
            len_1 = len(world[x1][y1])
            len_2 = len(world[x2][y2])
            if len_1 == 2 and len_2 ==2 : 
                if power_dic[world[x1][y1][1]] > power_dic[world[x2][y2][1]] : 
                    r1 = world[x1][y1][1] 
                else : 
                    r2 = world[x2][y2][1] 
            elif len_1 == 2 : 
                r1 = world[x1][y1][1] 
            elif len_2 == 2 :
                r2 = world[x2][y2][1]
            else : 
                div = True 
        
        if not div: 
            if r1 != 0 : 
                ret += power_dic[r1]
            if r2 != 0 :
                ret += power_dic[r2]
        else : 
            ret += power_dic[r1] #걍 두개 합 침
    return ret 
if __name__ == "__main__":
    test_case = int(input())
    for t in range(1,test_case+1): 
        m,a = map(int,input().split())
        world = [[deque() for _ in range(10)] for _ in range(10)] 
        player = [list(map(int,input().split())) for _ in range(2)]
        power = [list(map(int,input().split())) for _ in range(a)]
        power_dic = {} 
        power_range(power,world,power_dic)
        answer = moving(player,world,power_dic)
        print(f"#{t} {answer}")
    
    
"""
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70

1
5 4
0 0 0 0 0 
0 0 0 0 0 
1 2 1 100
9 10 1 100
10 9 1 200
9 9 2 300


1
5 3
0 0 0 0 0 
0 0 0 0 0 
1 2 1 100
9 10 1 100
6 3 2 70
"""