n = int(input())
like = {} 
for _ in range(n**2): 
    temp = list(map(int,input().split())) 
    like[temp[0]] = temp[1:]
world = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def search(index,st_num,st_like):
    if index == 0 : 
        world[1][1] = st_num 
    else :  
        cnt_ij = 0
        position_ij = [] 
        for i in range(n):
            for j in range(n): 
                if world[i][j] == 0 :
                    cnt = 0  
                    for px,py in zip (dx,dy): 
                        nx,ny = i+px, j+py 
                        if 0<=nx<n and 0<=ny<n and world[nx][ny] in st_like : 
                            cnt+=1 
                    if cnt_ij < cnt :
                        position_ij = [(i,j)]
                        cnt_ij = cnt 
                    elif cnt_ij == cnt : 
                        position_ij.append((i,j))
        len_position = len(position_ij)
        if len_position ==1 : 
            x,y = position_ij[0][0], position_ij[0][1] 
            world[x][y] = st_num 
       
        elif len_position > 1 or cnt_ij == 0: 
            cnt_ori = 0 
            wx,wy = -1,-1
            for x,y in position_ij : 
                cnt_dest = 0 
                for px,py in zip(dx,dy):
                    nx,ny = x+px,y+py 
                    if 0<=nx<n and 0<=ny<n and world[nx][ny]==0 :
                        cnt_dest += 1 
                if cnt_dest > cnt_ori : 
                    wx,wy = x,y 
                    cnt_ori = cnt_dest 
                elif cnt_dest == cnt_ori : 
                    if wx>x : 
                        wx,wy = x,y 
                    elif wx==x and wy>y : 
                        wx,wy = x,y 
            if cnt_ori == 0 : 
                wx,wy= position_ij[0][0], position_ij[0][1]
            world[wx][wy] = st_num 

def point(like):
    ret =0
    for i in range(n):
        for j in range(n): 
            cnt = 0 
            for px,py in zip(dx,dy):
                nx,ny = i+px,j+py 
                if 0<=nx<n and 0<=ny<n and world[nx][ny] in like[world[i][j]] :
                    cnt+=1
            ret+= int(10**(cnt-1))
    return ret 

for i,num in enumerate(like.keys()) :
    search(i,num,like[num])

# for w in world:
#     print(w)

print(point(like))




    