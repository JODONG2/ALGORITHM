
def snail_array(n):
    num = 1 
    limit = n **2  
    arr = [[0 for _ in range(n)] for _ in range(n)] 
    i=0
    j=0
    for _ in range(n):
        arr[i][j] = num
        num+=1
        j+=1
    j-=1
    while num < limit : 
            n -= 1 
            for _ in range(n):
                if num == limit : 
                    break
                i+=1
                arr[i][j] = num 
                num+=1
            for _ in range(n):
                if num == limit : 
                    break
                j-=1
                arr[i][j]=num 
                num+=1
            n-=1 
            for _ in range(n):
                if num == limit : 
                    break
                i-=1 
                arr[i][j] = num
                num+=1
            for _ in range(n):
                if num == limit:
                    break
                j+=1
                arr[i][j] = num 
                num+=1 
    for ar in arr:
        print(ar)

snail_array(5)