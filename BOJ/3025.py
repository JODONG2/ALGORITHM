import sys
def gravity(x,j,y):
    for i in range(x,r-1):
        dp[y].append((i,j))
        if maps[i+1][j] == 'X':
            maps[i][j] = 'O' 
            return
        elif maps[i+1][j] == 'O':
            if 0<=j-1  and maps[i][j-1] =='.' and maps[i+1][j-1] == '.':
                j-=1 
                if i+1 == r-1: 
                    maps[i+1][j] = 'O'
            elif j+1<c and maps[i][j+1] =='.' and maps[i+1][j+1] =='.': 
                j+=1
                if i+1 == r-1 : 
                    maps[i+1][j] = 'O'
            else:
                maps[i][j] = 'O'
                return
        elif i == r-2 : 
            dp[y].append((i+1,j))
            maps[i+1][j] = 'O'
            

r,c = map(int,sys.stdin.readline().split())
maps = [list(sys.stdin.readline()[:-1]) for _ in range(r)]
cnt = int(sys.stdin.readline())
dp = [[(0,i)] for i in range(c)]

for _ in range(cnt):
    j = int(sys.stdin.readline())
    j-=1
    x,y = dp[j].pop()
    while dp[j] and maps[x][y] !='.': 
        x,y = dp[j].pop()
    gravity(x,y,j)
for m in maps:
    m = ''.join(m)
    print(m)

"""
7 6
......
......
...XX.
......
......
.XX...
......
7
1
4
4
6
4
4
4

7 6
......
......
...XX.
......
......
.XX...
......
6
1
4
4
6
4
4

"""