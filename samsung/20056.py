
n,m,k = map(int,input().split()) 

fire = {}
fk = 1
for _ in range(1,m+1): 
    fire[fk] = list(map(int,input().split()))
    fire[fk][0]-=1
    fire[fk][1]-=1
    fk+=1 
direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
#ri, ci, mi, si, di
def command(fire,k): 
    global fk 
    world = [[[0,0,0,0,0,True] for _ in range(n)] for _ in range(n)]
    for _ in range(k) : 
        fire_list = list(fire.keys())
        # print(fire_list)
        for key in fire_list:
            r,c,m,s,d = fire[key] 
            r,c = (r+direction[d][0]*s)%n, (c+direction[d][1]*s)%n
            if world[r][c][0] != 0 : #이미 존재하면 ?! m,s,d,cnt 
                world[r][c][0] += m 
                world[r][c][1] += s
                if world[r][c][5] and world[r][c][2] != d%2:
                    world[r][c][5] = False 
                world[r][c][3] +=1
                del fire[key] 
            else : 
                world[r][c][0] = m 
                world[r][c][1] = s 
                world[r][c][2] = d%2 
                world[r][c][3] = 1 
                world[r][c][4] = key 
                fire[key][0],fire[key][1] = r,c
        # for w in world:
        #     print(w)
        # print("%"*100)
        for i in range(n):
            for j in range(n):
                if world[i][j][3] == 0 : 
                    continue 
                if world[i][j][3]>1 :
                    m,s,d,cnt,key,check = world[i][j]
                    d = 0 if check else 1
                    m = m // 5
                    if m != 0 : 
                        s = s//cnt 
                        for dir in range(d,8,2):
                            fire[fk] = [i,j,m,s,dir]
                            fk+=1 
                    del fire[key]
                world[i][j] = [0,0,0,0,0,True]
        
command(fire,k)
answer = 0 
# print(fire)
for value in fire.values():
    answer+=value[2]
print(answer)
'''
3 8 4
1 1 3 1 3 
1 2 3 1 4 
1 3 3 1 5 
2 1 3 1 2 
2 3 3 1 6
3 1 3 1 1 
3 2 3 1 0 
3 3 3 1 7 

3 3 3 
1 2 5 1 2 
2 2 5 1 1 
2 3 5 1 0

4 2 2
1 1 5 2 2
1 4 7 1 6

3 3 10 
1 1 5 2 2
1 2 5 2 2
1 3 5 2 2

3 3 10 
1 1 5 2 3
2 2 5 2 3
3 3 5 2 1

3 3 10 
1 1 5 1 3
2 2 5 1 3
3 3 5 1 1

4 9 5
3 2 8 5 2
3 3 19 3 4
3 1 7 1 1
4 4 6 4 0
2 1 6 2 5
4 3 9 4 3
2 2 16 1 2
4 2 17 5 3
3 4 3 5 7
->33
'''
            