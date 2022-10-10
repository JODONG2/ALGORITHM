import sys 

def f(cnt,sum, index ):
    if cnt == n//2 :
        global ans 
        ans = min(abs(sum - total), ans)
        return 
    
    for i in range(index+1,n):
        sum+= src[i] 
        f(cnt+1 , sum , i) 
        sum-= src[i]

n = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 
src = [0 for _ in range(n)]
total = 0 
ans = float('inf')
for i in range(n):
    for j in range(n):
        total += matrix[i][j] 
        src[i] += matrix[i][j] 
        src[j] += matrix[i][j] 
f(1,src[0],0)
print(ans)