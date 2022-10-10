n,m= map(int,input().split())
arr = [[i*n+j for j in range(n)] for i in range(n)]
for a in arr:
    print(a)

def right_90(arr):
    ret = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j] 
    for r in ret :
        print(r)

def left_90(arr):
    ret = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n): 
        for j in range(n):
            ret[n-1-j][i]=arr[i][j]
    for r in ret:
        print(r)

def snail(n,m):
    ret = [[0 for _ in range(m)] for _ in range(n)]
    num = 1 
    i,j = 0,0
    while n > 0 or m > 0: 
        for _ in range(m):
            ret[i][j] = num
            j+=1 
            num+=1 
        j -=1 
        i += 1 
        n-=1 
        if n ==0 :
            break 
        for _ in range(n): 
            ret[i][j] = num
            num+=1 
            i+=1 
        i-=1 
        j-=1 
        m-=1 
        if m == 0 :
            break 
        for _ in range(m): 
            ret[i][j] = num 
            num+=1 
            j-=1 
        j+=1 
        i-=1 
        n-=1 
        if n ==0 : break 
        for _ in range(n): 
            ret[i][j] = num 
            i-=1 
            num+=1 
        i+=1 
        j+=1 
        m-=1 
        if m == 0 : break 
    for r in ret:
        print(r)
        

print('right 90')
right_90(arr)
print('left 90')
left_90(arr)
print('snail')
snail(n,m)