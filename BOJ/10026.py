#https://www.acmicpc.net/problem/10026
from collections import deque 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N = int(input())

def dfs(arr,I,J,area,cnt):
    Q = deque()
    Q.append([I,J])
    while Q:
        i,j = Q.pop()
        for d in range(4):
            new_i = i+dy[d]
            new_j = j+dx[d]
            if 0<= new_i< N and 0<= new_j <N and not [new_i,new_j] in Q:
                if arr[i][j] == arr[new_i][new_j] and area[new_i][new_j] == 0:
                    area[new_i][new_j] = cnt
                    #dfs(arr,new_i,new_j,area,cnt)
                    Q.append([new_i,new_j])
            
RB = []
RGB = []
for _ in range(N):
    rgb = input()
    RGB.append(list(rgb))
    RB.append(list(rgb.replace('G','R')))
rgb_area = [[0 for _ in range(N)] for _ in range(N)]
rb_area = [[0 for _ in range(N)] for _ in range(N)]
rgb_count = 1
rb_count = 1
for i in range(N):
    for j in range(N):
        if rgb_area[i][j] == 0 :
            dfs(RGB,i,j,rgb_area,rgb_count)
            rgb_count+=1 
        if rb_area[i][j] == 0 :
            dfs(RB,i,j,rb_area,rb_count)
            rb_count+=1 

print(rgb_count-1, rb_count-1)
