import sys 
from collections import deque 
dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,1,0,-1,1,0,-1]
def f1(k):
    global answer 
    newt = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        for i in range(n):
            for j in range(n): 
                if space[i][j] : 
                    temp = deque()
                    plus_energy = 0
                    while space[i][j] : 
                        age = space[i][j].popleft()
                        if energy[i][j] - age >= 0 :
                            energy[i][j] -= age
                            temp.append(age+1)
                            if (age+1) % 5 == 0 : 
                                newt[i][j] += 1 
                        else : 
                            plus_energy += age//2 
                            answer-=1
                    energy[i][j]+= plus_energy
                    space[i][j] = deque([t for t in temp])

        for i in range(n):
            for j in range(n):
                energy[i][j] += plus[i][j] 
                if newt[i][j] >0 : 
                    for pi,pj in zip (dx,dy):
                        ni,nj = i+pi,j+pj 
                        if 0<=ni<n and 0<=nj<n : 
                            for _ in range(newt[i][j]):
                                space[ni][nj].appendleft(1)
                                answer+=1
                    newt[i][j] = 0


   

n,m,k = map(int,sys.stdin.readline().split()) 
plus = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
space = [[deque()for _ in range(n)] for _ in range(n)]
energy = [[5 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,a = map(int,sys.stdin.readline().split())
    x-=1
    y-=1
    space[x][y].append(a)
answer =m
f1(k)
print(answer)


