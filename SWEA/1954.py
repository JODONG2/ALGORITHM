tc = int(input()) 

for t in range(1,tc+1):
    n = int(input()) 
    arr = [[0 for _ in range(n)] for _ in range(n)] 
    i,j = 0,0
    num = 1 
    while n != 0 :
        for _ in range(n) : 
            arr[i][j] = num 
            num+=1 
            j+=1
        j-=1 
        i+=1 # 오른쪽 위 모서리 
        n -= 1 # 개수 -=1 
        if n == 0 : 
            break 
        for _ in range(n):
            arr[i][j] = num 
            num+=1 
            i+=1 
        i-=1
        j-=1 # 오른쪽 아래 모서리 
        for _ in range(n) : 
            arr[i][j] = num 
            num+=1 
            j-=1 
        j+=1 
        i-=1 #왼쪽 아래 모서리 
        n-=1 
        if n == 0 :
            break 
        for _ in range(n): 
            arr[i][j] = num 
            num+=1 
            i-=1 
        i+=1 
        j+=1 
    print(f"#{t}")
    for a in arr:
        print(' '.join((map(str,a))))
