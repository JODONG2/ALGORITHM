import sys 
from collections import deque 

def copy(world):
    ret = {} 
    for key,value in list(world.items()):
        ret[key] = deque([v for v in value])
    return ret

dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
def fish_move(world,shark,smell):
    key_list = world.keys() 
    ret = {}
    for key in key_list : 
        sequence = {}
        x,y = key 
        while world[key]: 
            d = world[key].pop()
            if sequence.get(d) : 
                ret[(sequence[d][0],sequence[d][1])].append(sequence[d][2])
                continue
            succ = False 
            for spin in range(8): 
                d2 = d - spin
                nx,ny = x+dir[(d2)%8][0], y+dir[(d2)%8][1]
                if 1<=nx<5 and 1<=ny<5 and shark!=[nx,ny] and not smell.get((nx,ny)) : 
                    succ = True 
                    sequence[d] = (nx,ny,d2)
                    if ret.get((nx,ny)): 
                        ret[(nx,ny)].append(d2%8)
                    else : 
                        ret[(nx,ny)] = deque([d2%8])
                    break 
            if not succ : 
                sequence[d] = (x,y,d)
                if ret.get((x,y)) : 
                    ret[(x,y)].append(d)
                else :
                    ret[(x,y)] = deque([d])
    return ret 

shark_dir = [(-1,0),(0,-1),(1,0),(0,1)]

def shark_move(world,shark,smell,maxi,depth,rw,rsh,rsm,ret):
    if depth == 3 : 
        if ret < maxi : 
            return world,shark,smell,maxi
        return rw,rsh,rsm,ret 

    x,y = shark 
    
    for dx,dy in (shark_dir) : 
        nx,ny = x+dx,y+dy 
        if 1<=nx<5 and 1<=ny<5 : 
            catch = 0 
            temp_w = {}
            temp_s = {}
            for key,value in list(smell.items()):
                temp_s[key] = value
            for key, value in list(world.items()):
                if key == (nx,ny):
                    catch += len(world[key])
                    temp_s[(nx,ny)] = 2
                    continue  
                temp_w[key] = deque([v for v in value])
            rw,rsh,rsm,ret = shark_move(temp_w,[nx,ny],temp_s,maxi+catch,depth+1,rw,rsh,rsm,ret)
    return rw,rsh,rsm,ret


if __name__ =="__main__":
    m, s= map(int,sys.stdin.readline().split())
    world = {} 
    for _ in range(m): 
        x,y,d= (map(int,sys.stdin.readline().split())) 
        if world.get((x,y)): 
            world[(x,y)].append(d-1)
        else: 
            world[(x,y)] = deque([d-1])
    shark = list(map(int,sys.stdin.readline().split()))
    smell = {}
    for _ in range(s) :
        fish_copy = copy(world)

        world = fish_move(world,shark,smell)
        for key in list(smell.keys()): 
            smell[key] -=1 
            if smell[key] == 0 : 
                del smell[key]

        world,shark,smell,temp = shark_move(world,shark,smell,0,0,{},[],{},-1)
        for key,value in list(fish_copy.items()):
            if world.get(key) : 
                for v in value : 
                    world[key].append(v)
            else : 
                world[key] = deque([v for v in value])
    answer = 0
    for key in list(world.keys()):
        answer+= len(world[key])
    print(answer)
    

"""
5 4
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
"""
    


