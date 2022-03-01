import sys
from collections import deque
def data_input(): 
    M,N,kch = map(int,sys.stdin.readline().split())
    fields = [[0 for _ in range(M)] for _ in range(N)] 
    positions = []
    for _ in range(kch):
        x,y = map(int,sys.stdin.readline().split())
        fields[y][x] = 1 
        positions.append((x,y))
    return M,N,fields,positions

def connect_component(fields,positions,N,M)->int:
    dx = [0,0,-1,1]
    dy = [1,-1,0,0] 
    positions = deque(positions)
    answer = 0 
    while positions : 
        x,y = positions.popleft()
        fields[y][x] = 0 
        answer += 1
        q = deque([(x,y)])
        while q :
            x,y = q.popleft()
            for px, py in zip(dx,dy): 
                nx,ny = x+px, y+py
                if 0<=nx<M and 0<=ny<N and fields[ny][nx] == 1 :
                    del positions[positions.index((nx,ny))]
                    q.append([nx,ny])
                    fields[ny][nx] = 0
    return answer 

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        M,N,fields,positions = data_input()
        answer= connect_component(fields,positions,N,M)
        print(answer)
        
"""

2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

"""