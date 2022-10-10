R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
check = [[0]*C for _ in range(R)]

A = ord('A')
stack = [(0,0,1,1<<(ord(arr[0][0])-A))]
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
while stack:
    x,y,cnt,total = stack.pop()
    if result < cnt:
        result = cnt
    if result == 26:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0<= ny <C:
            if (total & (1<<ord(arr[nx][ny])- A)) == 0:
                temp = total | (1<<(ord(arr[nx][ny])-A))
                if check[nx][ny] != temp:
                    check[nx][ny] = temp
                    stack.append((nx,ny,cnt+1,temp))
print(result)