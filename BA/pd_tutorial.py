import sys

def recur(si,sj,N):
    global ans
    global num
    if N == 2 :
        for i in range(2):
            for j in range(2):
                # arr[si+i][sj+j] = num
                if si+i == r and sj+j == c:
                    ans = num
                    return
                num+=1
        return
    quant = N//2
    for i in range(si,si+N,quant):
        for j in range(sj,sj+N,quant):
            if i<= r < i+quant and j<= c < j+quant :
                recur(i,j,quant)
            else:
                num += quant**2
if __name__ == '__main__':
    
    n,r,c = map(int,sys.stdin.readline().split())
    num = 0
    ans = 0
    N = 2**n
    recur(0,0,N)
    print(ans)