
import sys 
from collections import deque 
#1 : 동 y+1 
#2 : 서 y-1 
#3 : 남 x+1
#4 : 북 x-1

def change(dice_num, world_num):
    if world_num == 0: 
        world_num = dice_num 
    else : 
        dice_num = world_num 
        world_num = 0 
    return world_num, dice_num 

def update_dice(row,col, command, world, x, y):
    new_num = world[x][y]
    if command == 1 : 
        new_bottom = row.pop()
        col_pop = col.pop()
        col.append(new_bottom) 
        row.appendleft(col_pop)
        new_num , row[1] = change(row[1], new_num)
        col[1] = row[1] 
        print(new_bottom)
    elif command == 2 : 
        new_bottom = row.popleft()
        col_pop = col.pop() 
        col.append(new_bottom)
        row.append(col_pop)
        new_num , row[1] = change(row[1], new_num)
        col[1] = row[1] 
        print(new_bottom)
    elif command == 3 : 
        col_pop = col.pop()
        col.appendleft(col_pop)
        new_num , col[1] = change(col[1], new_num)
        row[1] = col[1] 
        print(col[-1])
    elif command == 4 : 
        col_pop = col.popleft()
        col.append(col_pop)
        new_num , col[1] = change(col[1], new_num)
        row[1] = col[1] 
        print(col[-1])
    world[x][y] = new_num

def move_dice(command_dict,row, col):
    N,M,x,y,_ =  map(int,sys.stdin.readline().split())
    world = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    commands = list(map(int,sys.stdin.readline().split()))
    for command in commands: 
        px,py = command_dict[command]
        if 0<= x + px < N and 0<= y + py <M :
            x = x+px 
            y = y+py
            update_dice(row,col, command, world,x,y)

if __name__ == "__main__":
    command_dict = { 1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0) }
    row = deque([0,0,0])
    col = deque([0,0,0,0])

    move_dice(command_dict, row, col)
    